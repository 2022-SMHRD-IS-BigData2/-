from pydantic import BaseModel,Field
import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from typing import Union

class Patient(BaseModel):
  pid : int
  birth_date: datetime.date
  sex : int
  age : int
  name : str
  emp_id : int
  admin_date : datetime.datetime=datetime.datetime.now()
  disch_date: datetime.datetime=None

class RecordNormal(BaseModel):
  pid : int
  p_record_seq : int
  birth_date :datetime.date
  input_time : datetime.datetime
  sex :int
  age: int
  hr: int
  temp: float
  resp: int
  sbp: int
  dbp: int
  ICULOC : int
  sepsis_in_six:int
  sepsis_percent:float

class Record(BaseModel):
  pid : int
  # p_record_seq : int
  birth_date :datetime.date
  input_time : datetime.datetime
  sex: int
  # p_age: int
  hr: int
  temp: float
  resp: int
  sbp: int
  dbp: int
  ICULOC : int
  BaseExcess:float
  HCO3:float
  FiO2:float
  pH:float
  PaCO2:float
  SaO2:float
  Alkalinephos:float
  Calcium:float
  Chloride:float
  Creatinine:float
  Bilirubin_direct:float
  Glucose:float
  Lactate:float
  Phosphate:float
  Potassium:float
  Bilirubin_total:float
  TroponinI:float
  Hct:float
  Hgb:float
  PTT:float
  WBC:float
  Fibrinogen:float
  Platelets:float
  sepsis_in_six:int
  sepsis_percent:float

class Record_v(BaseModel):
  pid : int
  p_record_seq : int
  birth_date: datetime.date
  name : str
  age: int
  sex : int
  emp_id : int
  admin_date : datetime.datetime=datetime.datetime.now()
  disch_date : datetime.datetime=None
  input_time : datetime.datetime=datetime.datetime.now()
  hr: int
  temp: float
  resp: int
  sbp: int
  dbp: int
  ICULOC: int
  BaseExcess:float
  HCO3:float
  FiO2:float
  pH:float
  PaCO2:float
  SaO2:float
  Alkalinephos:float
  Calcium:float
  Chloride:float
  Creatinine:float
  Bilirubin_direct:float
  Glucose:float
  Lactate:float
  Phosphate:float
  Potassium:float
  Bilirubin_total:float
  TroponinI:float
  Hct:float
  Hgb:float
  PTT:float
  WBC:float
  Fibrinogen:float
  Platelets:float
  sepsis_in_six:int
  sepsis_percent:float

class Record_for_Predict:
  pid : int
  p_record_seq : int
  age : int
  hr: int
  temp: float
  resp: int
  bp: int
  sbp: int
  dbp: int


class Lab_Data:
  pid : int
  p_record_seq : int
  lab_record_seq: int
  BaseExcess:float
  HCO3:float
  FiO2:float
  pH:float
  PaCO2:float
  SaO2:float
  Alkalinephos:float
  Calcium:float
  Chloride:float
  Creatinine:float
  Bilirubin_direct:float
  Glucose:float
  Lactate:float
  Phosphate:float
  Potassium:float
  Bilirubin_total:float
  TroponinI:float
  Hct:float
  Hgb:float
  PTT:float
  WBC:float
  Fibrinogen:float
  Platelets:float