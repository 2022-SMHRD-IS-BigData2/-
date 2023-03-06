from pydantic import BaseModel
from typing import List, Optional,Tuple
import datetime
from fastapi.encoders import jsonable_encoder

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
class LabData(BaseModel):
  pid : int
#  lab_record_seq: int
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
  Phosphate:Optional[float] = None
  Potassium:Optional[float] = None
  Bilirubin_total:Optional[float] = None
  Hct:Optional[float] = None
  Hgb:Optional[float] = None
  PTT:Optional[float] = None
  WBC:Optional[float] = None
  Fibrinogen:Optional[float] = None
  Platelets:Optional[float] = None

  def to_query_values(self) -> Tuple:
    values = []
    columns = []
    for field, value in self.__dict__.items():
        if field != 'pid' and value is not None:
            columns.append(field)
            values.append(value)
    return tuple(values),
  def jsonable_encoder(self, exclude_unset=True, exclude_none=False):
    """
    Custom JSON serializer for LabData class.
    """
    data = {}
    for key, value in self:
        if exclude_unset and self.__fields__[key].default is value:
            continue
        if exclude_none and value is None:
            continue
        data[key] = value
    return data

