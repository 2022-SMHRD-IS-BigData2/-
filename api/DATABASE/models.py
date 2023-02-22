from sqlalchemy import Boolean, Column, Integer, FLOAT,String, DateTime, BigInteger, ForeignKey,DATE,DATETIME
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from db import Base
from db import ENGINE

import datetime

class PatientGeneralTable(Base):
  __tablename__='patient_general'
  p_id = Column(Integer, primary_key=True, autoincrement=True)
  birth_date = Column(Integer,nullable=False)
  sex=Column(Integer,nullable=False,)
  p_name=Column(String(50),nullable=False)
  emp_id=Column(Integer,nullable=False)
  admin_date=Column(DATE, nullable=False)
  disch_date=Column(DATE,nullable=True)

  vital_record_all = relationship("VitalRecordAll", back_populates="patient_general")


class VitalRecordAll(Base):
  __tablename__ = 'vital_record_all'
  record_id = Column(Integer, primary_key=True, autoincrement=True)
  p_id=Column(Integer,ForeignKey('patient_general.p_id'))
  birth_date=Column(Integer,nullable=False)
  input_time=Column(DATETIME,nullable=False)
  p_age=Column(Integer,nullable=False)
  hr=Column(Integer,nullable=False)
  p_temp=Column(FLOAT,nullable=False)
  resp=Column(Integer,nullable=False)
  sbp=Column(Integer,nullable=False)
  dbp=Column(Integer,nullable=False)
  BaseExcess=Column(FLOAT,nullable=True,default=0)
  HCO3=Column(FLOAT,nullable=True,default=0)
  FiO2=Column(FLOAT,nullable=True,default=0)
  pH=Column(FLOAT,nullable=True,default=0)
  PaCO2=Column(FLOAT,nullable=True,default=0)
  SaO2=Column(FLOAT,nullable=True,default=0)
  Alkalinephos=Column(FLOAT,nullable=True,default=0)
  Calcium=Column(FLOAT,nullable=True,default=0)
  Chloride=Column(FLOAT,nullable=True,default=0)
  Creatinine=Column(FLOAT,nullable=True,default=0)
  Bilirubin_direct=Column(FLOAT,nullable=True,default=0)
  Glucose=Column(FLOAT,nullable=True,default=0)
  Lactate=Column(FLOAT,nullable=True,default=0)
  Phosphate=Column(FLOAT,nullable=True,default=0)
  Potassium=Column(FLOAT,nullable=True,default=0)
  Bilirubin_total=Column(FLOAT,nullable=True,default=0)
  TroponinI=Column(FLOAT,nullable=True,default=0)
  Hct=Column(FLOAT,nullable=True,default=0)
  Hgb=Column(FLOAT,nullable=True,default=0)
  PTT=Column(FLOAT,nullable=True,default=0)
  WBC=Column(FLOAT,nullable=True,default=0)
  Fibrinogen=Column(FLOAT,nullable=True,default=0)
  Platelets=Column(FLOAT,nullable=True,default=0)
  sepsis_in_six=Column(Integer,nullable=True,default=0)
  sepsis_percent=Column(FLOAT,nullable=True,default=0)
  
  patient_general = relationship("PatientGeneralTable", back_populates="vital_record_all")

