from fastapi import FastAPI
from api.routes import patient_router, record_router,Security
from typing import List
from starlette.middleware.cors import CORSMiddleware

app=FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8002",
    "http://localhost:8081",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:8087",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['mysql://project-db-stu2.ddns.net:3308','*']
)

app.include_router(patient_router)
app.include_router(record_router)
app.include_router(Security)

