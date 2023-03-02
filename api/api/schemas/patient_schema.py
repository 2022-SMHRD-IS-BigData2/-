from pydantic import BaseModel
import datetime

class Patient(BaseModel):
  pid : int
  birth_date: datetime.date
  sex : int
  age : int
  name : str
  emp_id : int
  admin_date : datetime.datetime=datetime.datetime.now()
  disch_date: datetime.datetime=None
