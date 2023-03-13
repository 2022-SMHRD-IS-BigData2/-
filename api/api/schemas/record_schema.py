from pydantic import BaseModel
from typing import List, Optional,Tuple
import datetime
from fastapi.encoders import jsonable_encoder

class RecordNormal(BaseModel):
  pid : int
  p_record_seq : int
  birth_date :datetime.date
  input_time : datetime.datetime
  Gender :int
  Age: int
  HR: int
  O2Sat :float
  Temp: float
  Resp: int
  SBP: int
  DBP: int
  ICULOS : int
  sepsis_in_six:int
  sepsis_percent:float

# 입력을 위한 객체
class Record(BaseModel):
  pid : int
  # p_record_seq : int
  birth_date :datetime.date
  input_time : datetime.datetime
  Gender: int
  # p_age: int
  HR: int
  O2Sat :float
  Temp: float
  Resp: int
  SBP: int
  DBP: int
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
  Magnesium:float
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
  HR: int
  O2Sat :float
  Temp: float
  Resp: int
  SBP: int
  DBP: int

class Record_i(BaseModel):
  pid : int
  input_time: str
  birth_date: str
  Gender: int
  HR: int
  O2Sat :float
  Temp: float
  Resp: int
  SBP: int
  DBP: int
  
  sepsis_in_six: int=None
  sepsis_percent: float=None


# 보기 위한 객체
class Record_v(BaseModel):
  pid : int
  p_record_seq : int
  birth_date: datetime.date
  name : str
  Age: int
  Gender : int
  emp_id : int
  admin_date : datetime.datetime=datetime.datetime.now()
  disch_date : datetime.datetime=None
  input_time : datetime.datetime=datetime.datetime.now()
  HR: int
  O2Sat :float
  Temp: float
  Resp: int
  SBP: int
  DBP: int
  MAP:float
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
  Magnesium:float
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

class Record_for_Predict(BaseModel):
  Age : int
  HR: int
  O2Sat :float
  Temp: float
  Resp: int
  SBP: int
  DBP: int
  map:float
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
  Magnesium:float
  Phosphate:float
  Potassium:float
  Bilirubin_total:float
  Hct:float
  Hgb:float
  PTT:float
  WBC:float
  Fibrinogen:float
  Platelets:float
  age_mask: int = 0
  hr_mask: int = 0
  O2Sat_mask: int = 0
  temp_mask: int = 0
  resp_mask: int = 0
  sbp_mask: int = 0
  dbp_mask: int = 0
  map_mask: int = 0
  ICULOS_mask: int = 0
  EtCO2_mask: int = 0
  BaseExcess_mask: int = 0
  HCO3_mask: int = 0
  FiO2_mask: int = 0
  pH_mask: int = 0
  PaCO2_mask: int = 0
  SaO2_mask: int = 0
  AST_mask: int = 0
  BUN_mask: int = 0
  Alkalinephos_mask: int = 0
  Calcium_mask: int = 0
  Chloride_mask: int = 0
  Creatinine_mask: int = 0
  Glucose_mask: int = 0
  Lactate_mask: int = 0
  Magnesium_mask: int = 0
  Phosphate_mask: int = 0
  Potassium_mask: int = 0
  Bilirubin_total_mask: int = 0
  Hct_mask: int = 0
  Hgb_mask: int = 0
  PTT_mask: int = 0
  WBC_mask: int = 0
  Fibrinogen_mask: int = 0
  Platelets_mask: int = 0




# 랩 데이터만 따로 관리
class LabData(BaseModel):
  pid : int
#  lab_record_seq: int
  # Age : Optional[int] = None
  # HR: Optional[int] = None
  # O2Sat :Optional[float] = None
  # Temp: Optional[float] = None
  # Resp: Optional[float] = None
  # SBP: Optional[int] = None
  # DBP: Optional[int] = None
  EtCO2: Optional[float] = None
  BaseExcess:Optional[float] = None
  HCO3:Optional[float] = None
  FiO2:Optional[float] = None
  pH:Optional[float] = None
  PaCO2:Optional[float] = None
  SaO2:Optional[float] = None
  AST:Optional[float] = None
  BUN:Optional[float] = None
  Alkalinephos:Optional[float] = None
  Calcium:Optional[float] = None
  Chloride:Optional[float] = None
  Creatinine:Optional[float] = None
  Glucose:Optional[float] = None
  Lactate:Optional[float] = None
  Magnesium:Optional[float] = None
  Phosphate:Optional[float] = None
  Potassium:Optional[float] = None
  Bilirubin_total:Optional[float] = None
  Hct:Optional[float] = None
  Hgb:Optional[float] = None
  PTT:Optional[float] = None
  WBC:Optional[float] = None
  Fibrinogen:Optional[float] = None
  Platelets:Optional[float] = None


