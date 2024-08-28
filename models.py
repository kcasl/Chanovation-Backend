from pydantic import BaseModel

class SignUpSchema(BaseModel):
    email:str
    password:str

    class Config:
        schema_extra ={
            "example":{
                "email":"sample@gmail.com",
                "password":"sample123"
            }
        }

class LoginSchema(BaseModel):
    email:str
    password:str

    class Config:
        schema_extra ={
            "example":{
                "email":"sample@gmail.com",
                "password":"sample123"
            }
        }

class GetAddress(BaseModel):
    x_crd:str
    y_crd:str

    class Config:
        schema_extra ={
            "example":{
                "latitude":"37.56",
                "longitude":"127.32"
            }
        }

class PushLandmark(BaseModel):
    user_id:str
    token:str
    landmark:str
    durationtime:float

    class Config:
        schema_extra ={
            "example":{
                "user_id": "YEyabE8L2obLqTuobUVWlSNY8Dr1",
                "token":"Xkw19vgwf1k41kqgt91igjk1nddxbxjcb1ufijwl1u5uwu1op5ui1y49w",
                "landmark":"경복궁",
                "durationtime":123 # 분 단위로 기록할 것
            }
        }

# class GetLandmark(BaseModel):
#     token:str
#     landmark:str
#
#     class Config:
#         schema_extra ={
#             "example":{
#                 "email":"sample@gmail.com",
#                 "password":"samplepass123"
#             }
#         }

class RecordLandmark(BaseModel):
    user_id:str
    token:str
    landmark:str

    class Config:
        schema_extra = {
            "example": {
                "user_id":"YEyabE8L2obLqTuobUVWlSNY8Dr1",
                "token": "Xkw19vgwf1k41kqgt91igjk1nddxbxjcb1ufijwl1u5uwu1op5ui1y49w",
                "landmark": "경복궁"
            }
        }

class QueryLandmark(BaseModel):
    user_id: str
    token:str
    landmark:str

    class Config:
        schema_extra ={
            "example":{
                "user_id": "YEyabE8L2obLqTuobUVWlSNY8Dr1",
                "email":"sample@gmail.com",
                "password":"samplepass123"
            }
        }