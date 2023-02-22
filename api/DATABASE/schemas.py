from pydantic import BaseModel
import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Patient(BaseModel):
  p_id : int
  birth_date: int
  p_name : str
  sex : int
  emp_id : int
  admin_date : datetime.date=datetime.date.today()
  disch_date : datetime.date=None



class Record(BaseModel):
  record_id : int
  birth_date :int
  input_time : datetime.datetime
  p_age: int
  hr: int
  p_temp: float
  resp: int
  bp: int
  sbp: int
  dbp: int
  BaseExcess:float
  HCO3:float
  FiO2:float
  pH:float
  PaCO2:float
  SaO2:float
  ASAlkalinephos:float
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
