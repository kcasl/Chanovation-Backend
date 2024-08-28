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
    x_crd:str
    y_crd:str
    times:int

    class Config:
        schema_extra ={
            "example":{
                "user_id": "YEyabE8L2obLqTuobUVWlSNY8Dr1",
                "latitude":"37.56",
                "longitude":"127.32",
                "times":1 # 항상 1로 보낼것
            }
        }

class GetLandmark(BaseModel):
    user_id:str

    class Config:
        schema_extra ={
            "example":{
                "user_id": "YEyabE8L2obLqTuobUVWlSNY8Dr1"
            }
        }

class RecordLandmark(BaseModel):
    user_id:str
    idx:int

    class Config:
        schema_extra = {
            "example": {
                "user_id":"YEyabE8L2obLqTuobUVWlSNY8Dr1",
                "idx": 1
            }
        }

class QueryLandmark(BaseModel):
    query:str
    x_crd:str
    y_crd:str

    class Config:
        schema_extra ={
            "example":{
                "query":"경복궁",
                "latitude":"37.56",
                "longitude":"127.32"
            }
        }