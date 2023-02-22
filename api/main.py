from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from DATABASE.schemas import Patient,Record
from typing import List
from starlette.middleware.cors import CORSMiddleware
from db import session
from DATABASE.models import VitalRecordAll,PatientGeneralTable
from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
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
  temp=PatientGeneralTable()
  temp.p_id=mk_patient.p_id
  temp.birth_date=mk_patient.birth_date
  temp.sex=mk_patient.sex
  temp.emp_id=mk_patient.emp_id
  temp.admin_date=mk_patient.admin_date
  temp.p_name=mk_patient.p_name
  if mk_patient.disch_date:
    temp.disch_date=None
  else:
    temp.disch_date=mk_patient.disch_date
  session.add(temp)
  session.commit()
  return mk_patient

@app.get('/api/record/{p_id}')
async def p_record_all(p_id:int):
  p_record=session.query(VitalRecordAll).filter(VitalRecordAll.p_id==p_id).all()
  return p_record


  # mk_patient=PatientGeneralTable()
  # mk_patient.birth_date=birth
  # mk_patient.p_name=name
  # mk_patient.admin_date=admin_date

  # session.add(mk_patient)
  # session.commit()

  # return f"{name} 환자 등록 완료..."