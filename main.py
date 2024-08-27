import uvicorn
import pyrebase
import firebase_admin
from pydantic import BaseModel
from fastapi import FastAPI
from models import *
from fbconfig import firebaseConfig
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.requests import Request
from firebase_admin import credentials,auth

app = FastAPI()

if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_adminsdk.json")
    firebase_admin.initialize_app(cred)

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
            status_code=400,detail="Invalid Credentials"
        )

# 토큰 검증 및 사용자 고유 id 리턴
@app.post('/token')
async def validate_token(request:Request):
    headers = request.headers
    jwt = headers.get('authorization')

    user = auth.verify_id_token(jwt)

    return user["user_id"]

# 주변 지역의 랜드마크를 db에 기록
@app.post('/pushlm')
async def push_landmark(user_data:PushLandmark):
    pass

# 체류 시간 기반 랜드마크 후보군 선정
@app.post('/getlm')
async def get_landmark(request:Request):
    pass

# 최종 여행지 기록
@app.post('/recordlm')
async def record_landmark(user_data:RecordLandmark):
    pass

# 여행지 검색
@app.post('/querylm')
async def query_landmark(user_data:QueryLandmark):
    pass



if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)