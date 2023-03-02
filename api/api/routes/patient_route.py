from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey,text,and_
from sqlalchemy.orm import relationship
from datetime import datetime
import datetime
from ..models.patient_model import PatientGeneralTable
from ..schemas.patient_schema import Patient
from core.database import session

router = APIRouter()


@router.get('/api/patients')
async def index():
  patients=session.query(PatientGeneralTable).all()
  session.close()
  return patients

@router.get('/api/patients/{pid}')
async def index(pid:int):
  one_patient=session.query(PatientGeneralTable).filter(PatientGeneralTable.pid==pid).first()
  session.close()
  return one_patient


@router.post('/api/mk_patient')
async def mk_patient(mk_patient:Patient):
  query = text(f"insert into patient_general (birth_date, sex, name, emp_id) values ('{mk_patient.birth_date}', {mk_patient.sex}, '{mk_patient.name}', {mk_patient.emp_id})")
  session.execute(query)
  session.commit()
  query2="SELECT * FROM patient_general ORDER BY pid DESC LIMIT 1"
  patient=session.execute(query2)
  session.close()
  return patient

