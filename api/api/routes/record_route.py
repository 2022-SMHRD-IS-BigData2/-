from fastapi import APIRouter, Depends
from ..core.database import session
from typing import List,Tuple
from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey,text,and_,desc
from sqlalchemy.orm import relationship
from fastapi.encoders import jsonable_encoder
from api.models.record_model import *
from api.schemas.record_schema import *
import pandas as pd, numpy as np
from datetime import datetime
import datetime
import random


router = APIRouter()

median_values = {
    'EtCO2': 33.00,
    'BaseExcess': 0.00,
    'HCO3': 24.00,
    'FiO2': 0.50,
    'pH': 7.38,
    'PaCO2': 40.00,
    'SaO2': 97.00,
    'AST': 41.00,
    'BUN': 17.00,
    'Alkalinephos': 74.00,
    'Calcium': 8.30,
    'Chloride': 106.00,
    'Creatinine': 0.94,
    'Glucose': 127.00,
    'Lactate': 1.80,
    'Magnesium': 2.00,
    'Phosphate': 3.30,
    'Potassium': 4.10,
    'Bilirubin_total': 0.90,
    'Hct': 30.30,
    'Hgb': 10.30,
    'PTT': 32.40,
    'WBC': 10.30,
    'Fibrinogen': 250.00,
    'Platelets': 181.00
}




@router.get('/api/record/{pid}')
async def p_record_all(pid:int):
  p_record=session.query(AllPatientRecordView).filter(AllPatientRecordView.pid==pid).all()
  session.close()
  return p_record


@router.get("/api/data/")
async def get_data(limit: int = 10, page: int = 1):
  offset = (page - 1) * limit
  query = text(f"SELECT * FROM vital_record_now_view LIMIT :limit OFFSET :offset")
  result = session.execute(query, {"limit": limit, "offset": offset})
  data = [dict(row) for row in result]
  count = session.execute(text("SELECT COUNT(*) FROM vital_record_now_view")).fetchone()[0]
  session.close()
  return {"data": data, "count": count,'page':{'page':1,'limit':10}}

def model_predict(record:VitalRecordAll):
  per=round(random.random()*100,2)
  if per>50:
    record.sepsis_in_six=1
  else :
    record.sepsis_in_six=0
  record.sepsis_percent=per
  return record

# input window(batch) 숫자 정해지면 insult랑 predict 따로 분리시켜야겠다
@router.post("/api/input_record")
async def input_record(record :Record):
  temp=VitalRecordAll()
  temp.pid=record.pid
  # temp.p_record_seq=record.p_record_seq
  temp.birth_date=record.birth_date
  temp.input_time=datetime.datetime.now()
  # temp.p_age=record.p_age
  temp.hr=record.hr
  temp.O2Sat=record.O2Sat
  temp.temp=record.temp
  temp.resp=record.resp
  temp.sbp=record.sbp
  temp.dbp=record.dbp
  temp.ICULOS = record.ICULOS
  temp.BaseExcess=record.BaseExcess
  temp.HCO3=record.HCO3
  temp.FiO2=record.FiO2
  temp.pH=record.pH
  temp.PaCO2=record.PaCO2
  temp.SaO2=record.SaO2
  temp.Alkalinephos=record.Alkalinephos
  temp.Calcium=record.Calcium
  temp.Chloride=record.Chloride
  temp.Creatinine=record.Creatinine
  temp.Glucose=record.Glucose
  temp.Lactate=record.Lactate
  temp.Phosphate=record.Phosphate
  temp.Potassium=record.Potassium
  temp.Bilirubin_total=record.Bilirubin_total
  temp.Hct=record.Hct
  temp.Hgb=record.Hgb
  temp.PTT=record.PTT
  temp.WBC=record.WBC
  temp.Fibrinogen=record.Fibrinogen
  temp.Platelets=record.Platelets
  temp.sepsis_in_six=record.sepsis_in_six
  temp.sepsis_percent=record.sepsis_percent

  pred=model_predict(temp)
  session.add(pred)
  session.commit()
  session.close()
  return {"record":pred}

# 모든 환자의 최근 데이터를 가져오자(뷰를 만들었음) , 정철씨 안나옴!
@router.get('/api/get_latest_all')
async def get_latest_all():
  record=session.query(VitalRecordNowView).all()
  session.close()
  return record


# 모든 환자의 최근 데이터에서 한명의 환자 선택
@router.get('/api/get_latest_all/{pid}')
async def get_latest_all(pid:int):
  record=session.query(VitalRecordNowView).filter(VitalRecordNowView.pid==pid).all()
  session.close()
  return record

# sepsis 환자만 가져오기/페이징 들어갔음
@router.get('/api/get_latest_sepsis_all')
async def get_latest_sepsis_all(limit: int = 10, page: int = 1):
  offset = (page - 1) * limit
  query = text(f"SELECT * FROM now_view_sepsis LIMIT :limit OFFSET :offset")
  result = session.execute(query, {"limit": limit, "offset": offset}).all()
  data = [dict(row) for row in result]
  count = session.execute(text("SELECT COUNT(*) FROM now_view_sepsis")).fetchone()[0]
  session.close()
  return {"data": data, "count": count,'page':{'page':1,'limit':10}}

# sepsis 위험확률 80프로 넘는것만 / 페이징 들어갔음
@router.get('/api/get_latest_sepsis_percent')
async def get_latest_sepsis_percent(limit: int = 10, page: int = 1):
  offset = (page - 1) * limit
  query = text(f"SELECT * FROM vital_record_now_view where sepsis_percent>=80 LIMIT :limit OFFSET :offset")
  result = session.execute(query, {"limit": limit, "offset": offset}).all()
  data = [dict(row) for row in result]
  count = session.execute(text("SELECT COUNT(*) FROM vital_record_now_view where sepsis_percent>=80")).fetchone()[0]
  session.close()
  return {"data": data, "count": count,'page':{'page':1,'limit':10}}

# 
@router.get('/api/get_all_record')
async def get_all_record():
  record=session.query(AllPatientRecordView).all()
  session.close()
  return record

@router.get('/api/get_select_date')
async def get_select_date(pid:int,date:str):
  date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()  # 문자열 형식의 날짜를 datetime 객체로 변환
  record = session.query(AllPatientRecordView).filter(and_(AllPatientRecordView.pid == pid, AllPatientRecordView.input_time >= date_obj, AllPatientRecordView.input_time < date_obj + datetime.timedelta(days=1))).all()
  session.close()
  return record

# 검색기능~페이지 추가하면 딕셔너리부분에 추가해주면됨
@router.get('/api/get_search_data')
async def get_search_patient(path: str = '', search_str: str = '', limit: int = 10, page: int = 1):
    offset = (page - 1) * limit
    search_str = f"%{search_str}%" # 검색 문자열 앞뒤에 % 추가
    query = None
    count = None
    data=[]

    switch_path = {
        '/': f"SELECT * FROM vital_record_now_view WHERE (pid LIKE :search_str OR name LIKE :search_str) LIMIT :limit OFFSET :offset",
        '/detected': f"SELECT * FROM now_view_sepsis WHERE (pid LIKE :search_str OR name LIKE :search_str) LIMIT :limit OFFSET :offset",
    }
    switch_count = {
        '/': "SELECT COUNT(*) FROM patient_general WHERE (pid LIKE :search_str OR name LIKE :search_str)",
        '/detected': "SELECT COUNT(*) FROM now_view_sepsis WHERE (pid LIKE :search_str OR name LIKE :search_str)",
    }
    if path in switch_path:
        query = text(switch_path[path])
        count = session.execute(text(switch_count[path]), {"search_str": search_str}).fetchone()[0]

    if query is not None:
        result = session.execute(query, {"search_str": search_str, "limit": limit, "offset": offset}).all()
        data = [dict(row) for row in result]
    else:
        data = []

    return {"data": data, "count": count, "page": {"page": page, "limit": limit}}


# pid, input_time 입력받아서 그 시간의 record 가져오는 api
@router.get('/api/get_select_record/{pid}')
async def get_select_record(pid: int, input_time: str):
    input_time = datetime.datetime.strptime(input_time, '%Y-%m-%dT%H:%M:%S')
    query = text(f'select * from all_patients_vital_record_view where pid=pid and input_time=:input_time')
    record = session.execute(query, {"input_time": input_time}).first()
    session.close()
    return {"data": record}

# record 수정한 값 받아서 업데이트하는 api
@router.post('/api/update_record/{pid}')
async def update_record(pid:int, record_u:Record_u):
  query = text(f"UPDATE vital_record_all SET hr = :hr, O2Sat = :O2Sat, temp = :temp, resp = :resp, sbp = :sbp, dbp = :dbp WHERE pid = :pid AND p_record_seq = :p_record_seq")
  values = {'hr': record_u.hr, 'O2Sat': record_u.O2Sat, 'temp': record_u.temp, 'resp': record_u.resp, 'sbp': record_u.sbp, 'dbp': record_u.dbp, 'pid': pid, 'p_record_seq': record_u.p_record_seq}
    # 쿼리 실행
  session.execute(query,values)
  session.commit()
  updated_record = session.query(AllPatientRecordView).filter(AllPatientRecordView.pid == pid, AllPatientRecordView.p_record_seq == record_u.p_record_seq).first()
  session.close()
  return updated_record

def model_predict2(Record_i):
  per=round(random.random()*100,2)
  if per>50:
    Record_i.sepsis_in_six=1
  else :
    Record_i.sepsis_in_six=0
    Record_i.sepsis_percent=per
  return Record_i


# 환자 vital 5개 빠른추가
@router.post('/api/insert_fast_record/{pid}')
async def insert_fast_record(pid:int, record_i:Record_i):
  input_time = datetime.datetime.strptime(record_i.input_time, '%Y-%m-%dT%H:%M:%S')
  birth_date = datetime.datetime.strptime(record_i.birth_date, '%Y-%m-%d').date()

  model_predict2(record_i)
  query = text(f"INSERT INTO vital_record_all (pid, input_time, birth_date, sex, hr, temp, resp, sbp, dbp, sepsis_in_six, sepsis_percent) VALUES (:pid, :input_time, :birth_date, :sex, :hr, :O2Sat, :temp, :resp, :sbp, :dbp, :sepsis_in_six, :sepsis_percent)")
  values = {'pid': pid, 'input_time': input_time, 'birth_date': birth_date, 'sex': record_i.sex, 'hr': record_i.hr, 'O2Sat': record_i.O2Sat, 'temp': record_i.temp, 'resp': record_i.resp, 'sbp': record_i.sbp, 'dbp': record_i.dbp, 'sepsis_in_six': record_i.sepsis_in_six, 'sepsis_percent': record_i.sepsis_percent}
    # 쿼리 실행
  session.execute(query,values)
  session.commit()
  updated_record = session.query(AllPatientRecordView).filter(AllPatientRecordView.pid == pid, AllPatientRecordView.input_time == input_time).first()
  session.close()
  return updated_record


# 선택한 환자의 최근 7개 record를 가져오자
@router.get('/api/chart_records/{pid}')
async def chart_records(pid:int):
  
  query=text(f"SELECT * FROM all_patients_vital_record_view WHERE pid={pid} ORDER BY input_time DESC LIMIT 7")
  
  chart_records = session.execute(query).all()
  session.close()
  return chart_records

median_values = {
    "EtCO2": 33.00,
    "BaseExcess": 0.00,
    "HCO3": 24.00,
    "FiO2": 0.50,
    "pH": 7.38,
    "PaCO2": 40.00,
    "SaO2": 97.00,
    "AST": 41.00,
    "BUN": 17.00,
    "Alkalinephos": 74.00,
    "Calcium": 8.30,
    "Chloride": 106.00,
    "Creatinine": 0.94,
    "Glucose": 127.00,
    "Lactate": 1.80,
    "Magnesium": 2.00,
    "Phosphate": 3.30,
    "Potassium": 4.10,
    "Bilirubin_total": 0.90,
    "Hct": 30.30,
    "Hgb": 10.30,
    "PTT": 32.40,
    "WBC": 10.30,
    "Fibrinogen": 250.00,
    "Platelets": 181.00,
}
lab_cols=['pid','EtCO2',
      'BaseExcess', 'HCO3', 'FiO2', 'pH', 'PaCO2', 'SaO2', 'AST', 'BUN',
      'Alkalinephos', 'Calcium', 'Chloride', 'Creatinine',
      'Glucose', 'Lactate', 'Magnesium', 'Phosphate', 'Potassium',
      'Bilirubin_total', 'Hct', 'Hgb', 'PTT', 'WBC',
      'Fibrinogen', 'Platelets']

# lab data!!!!!!
@router.post('/api/lab_insert/{pid}')
async def lab_insert(pid:int,labdata: LabData):
    # -----------------lab_data_record 넣기--------------------------
  db_lab_data = LabDataRecord(**labdata.dict())
  session.add(db_lab_data)
  session.commit()
  
  # -----------------lab_data_filled 채우기-------------------
  df_fill_list = pd.read_sql(session.query(LabDataRecord).filter(LabDataRecord.pid==pid).statement, session.bind)

  for col in lab_cols:
    # pid의 첫번째 행(record_seq=1)들만 남긴다 => 인덱스 구해서 저장
    first_index = df_fill_list.drop_duplicates(['pid'], keep='first').index
    # train_df.loc[first_index,col]의 값: 각 pid의 첫번째 행들의 컬럼별 값들이 null이면 중앙값으로 채우고, 아니면 그냥 그대로 써라!
    df_fill_list.loc[first_index, col] = df_fill_list.loc[first_index,col].apply(lambda x:median_values[col] if pd.isna(x) else x)
    # 맨 앞이 null이면 중앙값으로 채웠으니까 ffill 써서 쭉 채워줌
    df_fill_list[col] = df_fill_list[col].fillna(method='ffill')
    db_lab_fill = LabDataFilled(**df_fill_list.iloc[-1].to_dict())
  session.add(db_lab_fill)
  session.commit()
# -----------------vital_record_all 최근 데이터 업데이트하기-----------
  latest_record = session.query(VitalRecordAll).filter_by(pid=pid).order_by(desc(VitalRecordAll.p_record_seq)).first()
  latest_filled = session.query(LabDataFilled).filter_by(pid=pid).order_by(desc(LabDataFilled.lab_record_seq)).first()
  if latest_filled:
    query = text("""
        UPDATE vital_record_all 
        SET EtCO2 = :EtCO2, BaseExcess = :BaseExcess, HCO3 = :HCO3, FiO2 = :FiO2, 
            pH = :pH, PaCO2 = :PaCO2, SaO2 = :SaO2, AST = :AST, BUN = :BUN, 
            Alkalinephos = :Alkalinephos, Calcium = :Calcium, Chloride = :Chloride, 
            Creatinine = :Creatinine, Glucose = :Glucose, Lactate = :Lactate, 
            Magnesium = :Magnesium, Phosphate = :Phosphate, Potassium = :Potassium, 
            Bilirubin_total = :Bilirubin_total, Hct = :Hct, Hgb = :Hgb, PTT = :PTT, 
            WBC = :WBC, Fibrinogen = :Fibrinogen, Platelets = :Platelets 
        WHERE pid = :pid AND p_record_seq = :p_record_seq
    """)
    values = {
        'EtCO2': latest_filled.EtCO2,
        'BaseExcess': latest_filled.BaseExcess,
        'HCO3': latest_filled.HCO3,
        'FiO2': latest_filled.FiO2,
        'pH': latest_filled.pH,
        'PaCO2': latest_filled.PaCO2,
        'SaO2': latest_filled.SaO2,
        'AST': latest_filled.AST,
        'BUN': latest_filled.BUN,
        'Alkalinephos': latest_filled.Alkalinephos,
        'Calcium': latest_filled.Calcium,
        'Chloride': latest_filled.Chloride,
        'Creatinine': latest_filled.Creatinine,
        'Glucose': latest_filled.Glucose,
        'Lactate': latest_filled.Lactate,
        'Magnesium': latest_filled.Magnesium,
        'Phosphate': latest_filled.Phosphate,
        'Potassium': latest_filled.Potassium,
        'Bilirubin_total': latest_filled.Bilirubin_total,
        'Hct': latest_filled.Hct,
        'Hgb': latest_filled.Hgb,
        'PTT': latest_filled.PTT,
        'WBC': latest_filled.WBC,
        'Fibrinogen': latest_filled.Fibrinogen,
        'Platelets': latest_filled.Platelets,
        'pid': pid,
        'p_record_seq': latest_record.p_record_seq
    }
    session.execute(query, values)
    session.commit()
  # ------------------vital_record_all 최근 batch 개 뽑아서 model pred 돌리기--------
  data_sat=session.query(VitalRecordAll).filter(VitalRecordAll.pid==pid).all()
  # 스케일링하기~
  # pred,percent = model(data_sat)
  # update해주기


  # ------------------vital_record_all 최근 데이터 sepsis업데이트하기--------------
@router.post('/api/vital_insert/{pid}')
async def vital_insert(pid:int,vital: Record_i):
  input_time = datetime.datetime.strptime(vital.input_time, '%Y-%m-%dT%H:%M:%S')
  birth_date = datetime.datetime.strptime(vital.birth_date, '%Y-%m-%d').date()
    # -----------------vital_record_all 만들기 넣기--------------------------
  latest_filled=session.query(LabDataFilled).filter(LabDataFilled.pid==pid).order_by(desc(LabDataFilled.lab_record_seq)).first()
  patient=session.execute(f"select * from patient_general where pid = {pid}")
  if latest_filled:
    query = text("""
        INSERT INTO vital_record_all (
            pid,input_time, birth_date, sex, age, hr, O2Sat, temp, resp, sbp, dbp,
            EtCO2, BaseExcess, HCO3, FiO2, 
            pH, PaCO2, SaO2, AST, BUN, 
            Alkalinephos, Calcium, Chloride, 
            Creatinine, Glucose, Lactate, 
            Magnesium, Phosphate, Potassium, 
            Bilirubin_total, Hct, Hgb, PTT, 
            WBC, Fibrinogen, Platelets 
        ) VALUES (
            :pid, :input_time, :birth_date, :sex, :age, :hr, :O2Sat, :temp, :resp, :sbp, :dbp,
            :EtCO2, :BaseExcess, :HCO3, :FiO2, 
            :pH, :PaCO2, :SaO2, :AST, :BUN, 
            :Alkalinephos, :Calcium, :Chloride, 
            :Creatinine, :Glucose, :Lactate, 
            :Magnesium, :Phosphate, :Potassium, 
            :Bilirubin_total, :Hct, :Hgb, :PTT, 
            :WBC, :Fibrinogen, :Platelets 
        )
      """)
    values = {
        'pid': pid,
        'input_time':input_time,
        'birth_date': birth_date,
        'sex': patient.sex,
        'age': patient.age,
        'hr': vital.hr,
        'O2Sat': vital.O2Sat,
        'temp': vital.temp,
        'resp': vital.resp,
        'sbp': vital.sbp,
        'dbp': vital.dbp,
        'EtCO2': latest_filled.EtCO2,
        'BaseExcess': latest_filled.BaseExcess,
        'HCO3': latest_filled.HCO3,
        'FiO2': latest_filled.FiO2,
        'pH': latest_filled.pH,
        'PaCO2': latest_filled.PaCO2,
        'SaO2': latest_filled.SaO2,
        'AST': latest_filled.AST,
        'BUN': latest_filled.BUN,
        'Alkalinephos': latest_filled.Alkalinephos,
        'Calcium': latest_filled.Calcium,
        'Chloride': latest_filled.Chloride,
        'Creatinine': latest_filled.Creatinine,
        'Glucose': latest_filled.Glucose,
        'Lactate': latest_filled.Lactate,
        'Magnesium': latest_filled.Magnesium,
        'Phosphate': latest_filled.Phosphate,
        'Potassium': latest_filled.Potassium,
        'Bilirubin_total': latest_filled.Bilirubin_total,
        'Hct': latest_filled.Hct,
        'Hgb': latest_filled.Hgb,
        'PTT': latest_filled.PTT,
        'WBC': latest_filled.WBC,
        'Fibrinogen': latest_filled.Fibrinogen,
        'Platelets': latest_filled.Platelets,
    }
  else:
    query = text("""
        INSERT INTO vital_record_all (
            pid, birth_date, sex, age, hr, O2Sat, temp, resp, sbp, dbp,
            EtCO2, BaseExcess, HCO3, FiO2, 
            pH, PaCO2, SaO2, AST, BUN, 
            Alkalinephos, Calcium, Chloride, 
            Creatinine, Glucose, Lactate, 
            Magnesium, Phosphate, Potassium, 
            Bilirubin_total, Hct, Hgb, PTT, 
            WBC, Fibrinogen, Platelets 
        ) VALUES (
            :pid, :birth_date, :sex, :age, :hr, :O2Sat, :temp, :resp, :sbp, :dbp,
            :EtCO2, :BaseExcess, :HCO3, :FiO2, 
            :pH, :PaCO2, :SaO2, :AST, :BUN, 
            :Alkalinephos, :Calcium, :Chloride, 
            :Creatinine, :Glucose, :Lactate, 
            :Magnesium, :Phosphate, :Potassium, 
            :Bilirubin_total, :Hct, :Hgb, :PTT, 
            :WBC, :Fibrinogen, :Platelets 
        )
      """)
    values = {
        'pid': pid,
        'input_time':input_time,
        'birth_date': birth_date,
        'sex': patient.sex,
        'age': patient.age,
        'hr': vital.hr,
        'O2Sat': vital.O2Sat,
        'temp': vital.temp,
        'resp': vital.resp,
        'sbp': vital.sbp,
        'dbp': vital.dbp,
        'EtCO2': median_values.EtCO2,
        'BaseExcess': median_values.BaseExcess,
        'HCO3': median_values.HCO3,
        'FiO2': median_values.FiO2,
        'pH': median_values.pH,
        'PaCO2': median_values.PaCO2,
        'SaO2': median_values.SaO2,
        'AST': median_values.AST,
        'BUN': median_values.BUN,
        'Alkalinephos': median_values.Alkalinephos,
        'Calcium': median_values.Calcium,
        'Chloride': median_values.Chloride,
        'Creatinine': median_values.Creatinine,
        'Glucose': median_values.Glucose,
        'Lactate': median_values.Lactate,
        'Magnesium': median_values.Magnesium,
        'Phosphate': median_values.Phosphate,
        'Potassium': median_values.Potassium,
        'Bilirubin_total': median_values.Bilirubin_total,
        'Hct': median_values.Hct,
        'Hgb': median_values.Hgb,
        'PTT': median_values.PTT,
        'WBC': median_values.WBC,
        'Fibrinogen': median_values.Fibrinogen,
        'Platelets': median_values.Platelets,
    }

    session.execute(query, values)
    session.commit()
  # ------------------vital_record_all 최근 batch 개 뽑아서 model pred 돌리기--------
  data_sat=session.query(VitalRecordAll).filter(VitalRecordAll.pid==pid).all()
  # pred,percent = model(data_sat)
  # 스케일링하기~
  # pred,percent = model(data_sat)
  # update해주기
  # ------------------vital_record_all 최근 데이터 sepsis업데이트하기--------------



