import uvicorn
import pyrebase
import firebase_admin
import requests
from pydantic import BaseModel
from fastapi import FastAPI
from models import *
from dbfunc import *
from kakaoapi import *
from fbconfig import firebaseConfig
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.requests import Request
from firebase_admin import credentials, auth, db, firestore

app = FastAPI()

if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_adminsdk.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://project-240825-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })

firebase = pyrebase.initialize_app(firebaseConfig)



# 회원가입
@app.post('/signup')
async def create_account(user_data:SignUpSchema):
    email = user_data.email
    password = user_data.password

    try:
        user = auth.create_user(
            email = email,
            password = password
        )

        return JSONResponse(content={"message" : f"User account created successfuly {user.uid}"},
                            status_code= 201
               )
    except auth.EmailAlreadyExistsError:
        raise HTTPException(
            status_code=400,
            detail= f"Account already created for the email {email}"
        )

# 로그인 및 토큰 발급
@app.post('/login')
async def create_access_token(user_data:LoginSchema):
    email = user_data.email
    password = user_data.password

    try:
        user = firebase.auth().sign_in_with_email_and_password(
            email = email,
            password = password,
        )

        token = user['idToken']


        return JSONResponse(
            content={
                "token":token
            },status_code=200
        )

    except:
        raise HTTPException(
            status_code=400,detail="이메일과 비밀번호를 확인해주세요."
        )

# 토큰 검증 및 사용자 고유 id 리턴
@app.post('/token')
async def validate_token(request:Request):
    headers = request.headers
    jwt = headers.get('authorization')

    user = auth.verify_id_token(jwt)

    return user["user_id"]

#주소 받아오기
@app.post('/getaddress')
async def get_address(user_data:GetAddress):
    x = float(user_data.x_crd)
    y = float(user_data.y_crd)
    address = get_users_address(x,y)

    return address.split()[0]

# 주변 지역의 랜드마크를 db에 기록
@app.post('/pushlm')
async def push_landmark(user_data:PushLandmark):
    try:
        x = float(user_data.x_crd)
        y = float(user_data.y_crd)
        address = get_users_address(x, y)

        ref = db.reference('landmark')

        data = {
            "location": address,
            "times": user_data.times
        }

        try:
            ref_val = db.reference('landmark').child(user_data.user_id)
            val = ref_val.get()

            if (list(val.values())[-1]["location"] == address):
                newdata = {
                    "location": address,
                    "times": list(val.values())[-1]["times"] + 1
                }
                ref_val.child(list(val.keys())[-1]).update(newdata)
                return JSONResponse(content={"message": "updated successfuly"})
            else:
                ref_val.push(data)
                return JSONResponse(content={"message": "pushed successfuly"})

        except Exception as e:
            ref.child(user_data.user_id).push(data)
            return JSONResponse(content={"message": "created successfuly"})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 체류 시간 기반 랜드마크 후보군 선정
@app.post('/getlm')
async def get_landmark(user_data:GetLandmark):
    try:
        ref = db.reference('landmark').child(user_data.user_id)
        val = ref.get()

        location_times = [(item.get("times", -float('inf')), item.get("location", None)) for item in val.values()]
        location_times.sort(key=lambda x: x[0], reverse=True)
        locations = {
            idx + 1: location for idx, (times, location) in enumerate(location_times[:3])
        }

        try:
            ref2 = db.reference('userselection').child(user_data.user_id)
            ref2.push(locations)

        except Exception as e:
            return f"error, {e}"

        return locations

    except Exception as e:
        return f"error, {e}"

# 최종 여행지 기록
@app.post('/recordlm')
async def record_landmark(user_data:RecordLandmark):
    try:
        idx = user_data.idx

        ref = db.reference('userselection').child(user_data.user_id)
        val = ref.get()

        final_record = list(val.values())[idx-1]

        try:
            ref2 = db.reference('selectionset').child(user_data.user_id)
            ref2.push(final_record[-1])

        except Exception as e:
            return f"error, {e}"

        return final_record[-1]

    except Exception as e:
        return f"error, {e}"

# 주변 여행지 검색
@app.post('/querylm')
async def query_landmark(user_data:QueryLandmark):
    x = float(user_data.x_crd)
    y = float(user_data.y_crd)
    q = user_data.query

    #print(search_places(q, x, y))

    return search_places(q, x, y)


if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)