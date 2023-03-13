from sqlalchemy import Boolean, Column, INT, FLOAT,String, DateTime, BigInteger, ForeignKey,DATE,DATETIME,INT
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from ..core.database import Base
import datetime

class PatientGeneralTable(Base):
  __tablename__='patient_general'
  pid = Column(INT, primary_key=True, autoincrement=True)
  birth_date = Column(DATE,nullable=False)
  Gender=Column(INT,nullable=False)
  Age=Column(INT,nullable=False)
  name=Column(String(50),nullable=False)
  emp_id=Column(INT,nullable=False)
  admin_date=Column(DATETIME, nullable=False)
  disch_date=Column(DATETIME,nullable=True)

  vital_record_all = relationship("VitalRecordAll", back_populates="patient_general")
  vital_record_all_mask = relationship("VitalRecordAllMask", back_populates="patient_general")



