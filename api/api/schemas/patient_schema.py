from pydantic import BaseModel
import datetime

class Patient(BaseModel):
  pid : int=None
  birth_date: datetime.date
  Gender : int
  Age : int=None
  name : str
  emp_id : int
  admin_date : datetime.datetime=datetime.datetime.now()
  disch_date: datetime.datetime=None
