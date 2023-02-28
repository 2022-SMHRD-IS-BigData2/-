from fastapi import FastAPI,Response
from fastapi.encoders import jsonable_encoder
from DATABASE.schemas import Patient,Record
from typing import List
from starlette.middleware.cors import CORSMiddleware
from db import session,Database
from DATABASE.models import VitalRecordAll,PatientGeneralTable,VitalRecordNowView,VitalRecordNowView,NowViewSepsis,AllPatientRecordView
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
    "http://localhost:8081",
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
  session.close()
  return patients

@app.get('/api/patients/{pid}')
async def index(pid:int):
  one_patient=session.query(PatientGeneralTable).filter(PatientGeneralTable.pid==pid).first()
  session.close()
  return one_patient



@app.post('/api/mk_patient')
async def mk_patient(mk_patient:Patient):
  query = text(f"insert into patient_general (birth_date, sex, p_name, emp_id) values ('{mk_patient.birth_date}', {mk_patient.sex}, '{mk_patient.p_name}', {mk_patient.emp_id})")
  session.execute(query)
  session.commit()
  query2="SELECT * FROM patient_general ORDER BY pid DESC LIMIT 1"
  patient=db.execute(query2)
  session.close()
  return patient

@app.get('/api/record/{pid}')
async def p_record_all(pid:int):
  p_record=session.query(AllPatientRecordView).filter(AllPatientRecordView.pid==pid).all()
  session.close()
  return p_record

@app.get("/api/all_from_view")
async def get_view():
  query = "SELECT * FROM vital_record_now_view"
  result=db.execute(query)

  data = [row for row in result]
  # data_json = json.dumps(data)

  return {"data": data}

@app.get("/api/data/")
async def get_data(limit: int = 10, page: int = 1):
    offset = (page - 1) * limit
    query = text(f"SELECT * FROM vital_record_now_view LIMIT :limit OFFSET :offset")
    result = session.execute(query, {"limit": limit, "offset": offset})
    data = [dict(row) for row in result]
    count = session.execute(text("SELECT COUNT(*) FROM vital_record_now_view")).fetchone()[0]
    return {"data": data, "count": count,'page':{'page':10,'limit':10}}

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
  temp.pid=record.pid
  # temp.p_record_seq=record.p_record_seq
  temp.birth_date=record.birth_date
  temp.input_time=datetime.datetime.now()
  # temp.p_age=record.p_age
  temp.hr=record.hr
  temp.temp=record.temp
  temp.resp=record.resp
  temp.sbp=record.sbp
  temp.dbp=record.dbp
  temp.ICULOC = record.ICULOC
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

  # 모든 환자의 최근 데이터를 가져오자(뷰를 만들었음) , 정철씨 안나옴!
@app.get('/api/get_latest_all')
async def get_latest_all():
  record=session.query(VitalRecordNowView).all()
  session.close()
  return record


# 모든 환자의 최근 데이터에서 한명의 환자 선택
@app.get('/api/get_latest_all/{pid}')
async def get_latest_all(pid:int):
  record=session.query(VitalRecordNowView).filter(VitalRecordNowView.pid==pid).all()
  session.close()
  return record

# sepsis 환자만 가져오기
@app.get('/api/get_latest_sepsis_all')
async def get_latest_sepsis_all():
  sepsis=session.query(NowViewSepsis).all()
  session.close()
  return sepsis

@app.get('/api/get_all_record')
async def get_all_record():
  record=session.query(AllPatientRecordView).all()
  session.close()
  return record

@app.get('/api/get_select_date?pid={pid}&input_time={date}')
async def get_select_date(pid:int,date:datetime.date):
  query="SELECT * FROM all_patients_vital_record_view WHERE DATE(input_time)=DATE('{date}') AND pid={pid}"
  record=db.execute(query)
  session.close()
  return record

@app.get('/api/get_search_patient')
async def get_search_patient(str:str):
  return "a"