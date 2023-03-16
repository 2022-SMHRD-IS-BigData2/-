from .database import Base,session
from sqlalchemy import Boolean, Column, INT, FLOAT,String, DateTime, BigInteger, ForeignKey,DATE,DATETIME
from pydantic import BaseModel
from typing import List, Optional,Tuple
import datetime
from fastapi import APIRouter,Depends
from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey,text,and_,desc
import pandas as pd, numpy as np

class TokenSepsis(Base):
  __tablename__ = 'token_sepsis'
  token_id=Column(INT, primary_key=True)
  user_id=Column(String, nullable=False)
  salt=Column(String, nullable=False)
  password = Column(String, nullable=False)
  IP=Column(String,nullable=False)
  token=Column(String,nullable=False)
  expire=Column(DATETIME,nullable=False)

class TokenSepsis_sche(BaseModel):
  token_id : int
  user_id : str
  salt : str
  password : str
  IP : str
  token :str
  expire: datetime.datetime

class User(BaseModel):
  user_id : str
  password : str
  IP : str
  salt: str=None

router=APIRouter()
from fastapi import FastAPI
from fastapi import Request, HTTPException, status, Depends,Header
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import secrets
import base64
# iv = secrets.token_bytes(16)
token=None
@router.post("/api/get_salt")
async def get_salt():
  # query=text(f"select salt from token_sepsis where user_id='{hashedId}'")
  # salt=session.execute(query).fetchone()
  salt=session.query(TokenSepsis).filter(TokenSepsis.user_id=="9ec62c20118ff506dac139ec30a521d12b9883e55da92b7d9adeefe09ed4e0bd152e2a099339871424263784f8103391f83b781c432f45eccb03e18e28060d2f").first()
  return salt

@router.post("/api/mk_token")
async def mk_token(User:User):
  query=text(f"select * from token_sepsis where user_id='{User.user_id}' and password='{User.password}' and IP='{User.IP}'")
  user_raw=session.execute(query).fetchone()
  if user_raw:
    global token
    token = secrets.token_hex(16)
    print(token)
    # print(token)
    return {"token":token}
  else:
    return {"status":"access failed.."}
  
# # 어찌합니까....
# async def check_token(request: Request):
#   token_user = request.headers.get("Authorization")
#   if not token_user:
#       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing token")
#   # 'Bearer' 문자열 제거
#   token_user = token_user[7:]
#   # 전역 변수에 저장된 토큰과 비교
#   if token_user != token:
#       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
#   return token_user
# from fastapi import Request, HTTPException, status

async def check_token(authorization: Optional[str] = Header(None)):
    if authorization is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing token")
    user_token = authorization[7:]
    if user_token != token: # 'token'이 어디서 정의되는지 확인하십시오.
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return user_token


