from fastapi import FastAPI,Response
from fastapi.encoders import jsonable_encoder
from DATABASE.schemas import Patient,Record
from typing import List
from starlette.middleware.cors import CORSMiddleware
from db import session,Database
from DATABASE.models import VitalRecordAll,PatientGeneralTable,VitalRecordNowView,VitalRecordNowView
from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey,text
from sqlalchemy.orm import relationship
import datetime
from pydantic import BaseModel
# from fastapi.staticfiles import StaticFiles
import random
import json
import sys
import os

sys.setrecursionlimit(10**7)

app=FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8002",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:8087",
    "http://localhost:8080",
    "*"
]

db=Database(app)

@app.on_event("startup")
async def startup_event():
    db.connect()

def get_db():
    try:
        db = session()
        yield db
    finally:
        db.close()

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['mysql://project-db-stu2.ddns.net:3307','*']
)

@app.get('/api/patients')
async def index():
  patients=session.query(PatientGeneralTable).all()

  return patients

@app.get('/api/patients/{p_id}')
async def index(p_id:int):
  one_patient=session.query(PatientGeneralTable).filter(PatientGeneralTable.p_id==p_id).first()
  return one_patient



@app.post('/api/mk_patient')
async def mk_patient(mk_patient:Patient):
  query = text(f"insert into patient_general (birth_date, sex, p_name, emp_id) values ('{mk_patient.birth_date}', {mk_patient.sex}, '{mk_patient.p_name}', {mk_patient.emp_id})")
  session.execute(query)
  session.commit()
  query2="SELECT * FROM patient_general ORDER BY p_id DESC LIMIT 1"
  patient=db.execute(query2)
  session.close()
  return patient

@app.get('/api/record/{p_id}')
async def p_record_all(p_id:int):
  p_record=session.query(VitalRecordAll).filter(VitalRecordAll.p_id==p_id).all()
  return p_record

@app.get("/api/all_from_view")
async def get_view():
  query = "SELECT * FROM vital_record_now_view"
  result=db.execute(query)

  data = [row for row in result]
  # data_json = json.dumps(data)

  return {"data": data}

def model_predict(record:VitalRecordAll):
  per=round(random.random()*100,2)
  if per>50:
    record.sepsis_in_six=1
  else :
    record.sepsis_in_six=0
  record.sepsis_percent=per
  return record

# input window(batch) 숫자 정해지면 insult랑 predict 따로 분리시켜야겠다
@app.post("/api/input_record")
async def input_record(record :Record):
  temp=VitalRecordAll()
  temp.p_id=record.p_id
  # temp.p_record_seq=record.p_record_seq
  temp.birth_date=record.birth_date
  temp.input_time=datetime.datetime.now()
  # temp.p_age=record.p_age
  temp.hr=record.hr
  temp.temp=record.p_temp
  temp.resp=record.resp
  temp.sbp=record.sbp
  temp.dbp=record.dbp
  # temp.ICULOC = record.ICULOC
  temp.BaseExcess=record.BaseExcess
  temp.HCO3=record.HCO3
  temp.FiO2=record.FiO2
  temp.pH=record.pH
  temp.PaCO2=record.PaCO2
  temp.SaO2=record.SaO2
  temp.Alkalinephos=record.Alkalinephos
  temp.Calcium=record.Calcium
  temp.Chloride=record.Chloride
  temp.Creatinine=record.Creatinine
  temp.Bilirubin_direct=record.Bilirubin_direct
  temp.Glucose=record.Glucose
  temp.Lactate=record.Lactate
  temp.Phosphate=record.Phosphate
  temp.Potassium=record.Potassium
  temp.Bilirubin_total=record.Bilirubin_total
  temp.TroponinI=record.TroponinI
  temp.Hct=record.Hct
  temp.Hgb=record.Hgb
  temp.PTT=record.PTT
  temp.WBC=record.WBC
  temp.Fibrinogen=record.Fibrinogen
  temp.Platelets=record.Platelets
  temp.sepsis_in_six=record.sepsis_in_six
  temp.sepsis_percent=record.sepsis_percent

  pred=model_predict(temp)
  session.add(pred)
  session.commit()
  session.close()
  return {"record":pred}

  # 모든 환자의 최근 데이터를 가져오자(뷰를 만들었음)
@app.get('/api/get_latest_all')
def get_latest_all():
  record=session.query(VitalRecordNowView).all()
  session.close()
  return record

# 모든 환자의 최근 데이터에서 한명의 환자 선택
@app.get('/api/get_latest_all/{pid}')
def get_latest_all(pid:int):
  record=session.query(VitalRecordNowView).filter(VitalRecordNowView.pid==pid).all()
  return record