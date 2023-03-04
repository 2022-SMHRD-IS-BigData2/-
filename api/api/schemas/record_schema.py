from pydantic import BaseModel
import datetime

class RecordNormal(BaseModel):
  pid : int
  p_record_seq : int
  birth_date :datetime.date
  input_time : datetime.datetime
  sex :int
  age: int
  hr: int
  O2Sat :float
  temp: float
  resp: int
  sbp: int
  dbp: int
  ICULOS : int
  sepsis_in_six:int
  sepsis_percent:float

# 입력을 위한 객체
class Record(BaseModel):
  pid : int
  # p_record_seq : int
  birth_date :datetime.date
  input_time : datetime.datetime
  sex: int
  # p_age: int
  hr: int
  O2Sat :float
  temp: float
  resp: int
  sbp: int
  dbp: int
  ICULOS : int
  EtCO2: float
  BaseExcess:float
  HCO3:float
  FiO2:float
  pH:float
  PaCO2:float
  SaO2:float
  AST:float
  BUN:float
  Alkalinephos:float
  Calcium:float
  Chloride:float
  Creatinine:float
  Glucose:float
  Lactate:float
  Phosphate:float
  Potassium:float
  Bilirubin_total:float
  Hct:float
  Hgb:float
  PTT:float
  WBC:float
  Fibrinogen:float
  Platelets:float
  sepsis_in_six:int
  sepsis_percent:float

class Record_u(BaseModel):
  pid : int
  p_record_seq : int
  hr: int
  O2Sat :float
  temp: float
  resp: int
  sbp: int
  dbp: int

class Record_i(BaseModel):
  pid : int
  input_time: str
  birth_date: str
  sex: int
  hr: int
  O2Sat :float
  temp: float
  resp: int
  sbp: int
  dbp: int
  sepsis_in_six: int=None
  sepsis_percent: float=None


# 보기 위한 객체
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
  O2Sat :float
  temp: float
  resp: int
  sbp: int
  dbp: int
  ICULOS: int
  EtCO2: float
  BaseExcess:float
  HCO3:float
  FiO2:float
  pH:float
  PaCO2:float
  SaO2:float
  AST:float
  BUN:float
  Alkalinephos:float
  Calcium:float
  Chloride:float
  Creatinine:float
  Glucose:float
  Lactate:float
  Phosphate:float
  Potassium:float
  Bilirubin_total:float
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

# 랩 데이터만 따로 관리
class Lab_Data:
  pid : int
  p_record_seq : int
  lab_record_seq: int
  EtCO2: float
  BaseExcess:float
  HCO3:float
  FiO2:float
  pH:float
  PaCO2:float
  SaO2:float
  AST:float
  BUN:float
  Alkalinephos:float
  Calcium:float
  Chloride:float
  Creatinine:float
  Glucose:float
  Lactate:float
  Phosphate:float
  Potassium:float
  Bilirubin_total:float
  Hct:float
  Hgb:float
  PTT:float
  WBC:float
  Fibrinogen:float
  Platelets:float