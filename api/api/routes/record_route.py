from fastapi import APIRouter, Depends
from ..core.database import session
from typing import List,Tuple
from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey,text,and_,desc
from sqlalchemy.orm import relationship
from fastapi.encoders import jsonable_encoder
from api.models.record_model import *
from api.models.patient_model import *
from api.schemas.record_schema import *
import pandas as pd, numpy as np
from datetime import datetime
import datetime
import random


router = APIRouter()

median_values = {
'hr': 84.58,
'O2Sat': 97.19,
'temp': 36.98,
'sbp': 123.75,
'dbp': 63.83,
'map': 82.40,
'resp': 18.73,
'EtCO2': 32.96,
'BaseExcess': -0.69,
'HCO3': 24.08,
'FiO2': 0.55,
'pH': 7.38,
'PaCO2': 41.02,
'SaO2': 92.65,
'AST': 260.22,
'BUN': 23.92,
'Alkalinephos': 102.48,
'Calcium': 7.56,
'Chloride': 105.83,
'Creatinine': 1.51,
'Glucose': 136.93,
'Lactate': 2.65,
'Magnesium': 2.05,
'Phosphate': 3.54,
'Potassium': 4.14,
'Bilirubin_total': 2.11,
'Hct': 30.79,
'Hgb': 10.43,
'PTT': 41.23,
'WBC': 11.45,
'Fibrinogen': 287.39,
'Platelets': 196.01
}
mean_values = {
    'hr': 84.58,
    'O2Sat': 97.19,
    'temp': 36.98,
    'sbp': 123.75,
    'dbp': 63.83,
    'map': 82.40,
    'resp': 18.73,
    'EtCO2': 32.96,
    'BaseExcess': -0.69,
    'HCO3': 24.08,
    'FiO2': 0.55,
    'pH': 7.38,
    'PaCO2': 41.02,
    'SaO2': 92.65,
    'AST': 260.22,
    'BUN': 23.92,
    'Alkalinephos': 102.48,
    'Calcium': 7.56,
    'Chloride': 105.83,
    'Creatinine': 1.51,
    'Glucose': 136.93,
    'Lactate': 2.65,
    'Magnesium': 2.05,
    'Phosphate': 3.54,
    'Potassium': 4.14,
    'Bilirubin_total': 2.11,
    'Hct': 30.79,
    'Hgb': 10.43,
    'PTT': 41.23,
    'WBC': 11.45,
    'Fibrinogen': 287.39,
    'Platelets': 196.01
}
std_values = {
    'hr': 17.33,
    'O2Sat': 2.94,
    'temp': 0.77,
    'sbp': 23.23,
    'dbp': 13.96,
    'map': 16.34,
    'resp': 5.10,
    'EtCO2': 7.95,
    'BaseExcess': 4.29,
    'HCO3': 4.38,
    'FiO2': 11.12,
    'pH': 0.07,
    'PaCO2': 9.27,
    'SaO2': 10.89,
    'AST': 855.75,
    'BUN': 19.99,
    'Alkalinephos': 120.12,
    'Calcium': 2.43,
    'Chloride': 5.88,
    'Creatinine': 1.81,
    'Glucose': 51.31,
    'Lactate': 2.53,
    'Magnesium': 0.40,
    'Phosphate': 1.42,
    'Potassium': 0.64,
    'Bilirubin_total': 4.31,
    'Hct': 5.49,
    'Hgb': 1.97,
    'PTT': 26.22,
    'WBC': 7.73,
    'Fibrinogen': 153.00,
    'Platelets': 103.64
}
vital_cols=['hr', 'O2Sat', 'temp', 'sbp', 'dbp', 'map', 'resp','EtCO2',
      'BaseExcess', 'HCO3', 'FiO2', 'pH', 'PaCO2', 'SaO2', 'AST', 'BUN',
      'Alkalinephos', 'Calcium', 'Chloride', 'Creatinine',
      'Glucose', 'Lactate', 'Magnesium', 'Phosphate', 'Potassium',
      'Bilirubin_total', 'Hct', 'Hgb', 'PTT', 'WBC',
      'Fibrinogen', 'Platelets']
COLSpp = ['HR', 'O2Sat', 'Temp', 'SBP', 'map', 'DBP', 'Resp', 'EtCO2',
          'BaseExcess', 'HCO3', 'FiO2', 'pH', 'PaCO2', 'SaO2', 'AST', 'BUN',
          'Alkalinephos', 'Calcium', 'Chloride', 'Creatinine',
          'Glucose', 'Lactate', 'Magnesium', 'Phosphate', 'Potassium',
          'Bilirubin_total', 'Hct', 'Hgb', 'PTT', 'WBC',
          'Fibrinogen', 'Platelets', 'Age']
INFO_COLS = ['pid', 'HospAdmTime', 'ICULOS', 'SepsisLabel', 'Age','Gender']

lab_cols=['pid','EtCO2',
      'BaseExcess', 'HCO3', 'FiO2', 'pH', 'PaCO2', 'SaO2', 'AST', 'BUN',
      'Alkalinephos', 'Calcium', 'Chloride', 'Creatinine',
      'Glucose', 'Lactate', 'Magnesium', 'Phosphate', 'Potassium',
      'Bilirubin_total', 'Hct', 'Hgb', 'PTT', 'WBC',
      'Fibrinogen', 'Platelets']
lab_cols2=['EtCO2',
      'BaseExcess', 'HCO3', 'FiO2', 'pH', 'PaCO2', 'SaO2', 'AST', 'BUN',
      'Alkalinephos', 'Calcium', 'Chloride', 'Creatinine',
      'Glucose', 'Lactate', 'Magnesium', 'Phosphate', 'Potassium',
      'Bilirubin_total', 'Hct', 'Hgb', 'PTT', 'WBC',
      'Fibrinogen', 'Platelets','sepsis_in_six','sepsis_percent']
lab_cols3=['EtCO2',
      'BaseExcess', 'HCO3', 'FiO2', 'pH', 'PaCO2', 'SaO2', 'AST', 'BUN',
      'Alkalinephos', 'Calcium', 'Chloride', 'Creatinine',
      'Glucose', 'Lactate', 'Magnesium', 'Phosphate', 'Potassium',
      'Bilirubin_total', 'Hct', 'Hgb', 'PTT', 'WBC',
      'Fibrinogen', 'Platelets']

COLS = ['age', 'hr', 'O2Sat', 'temp', 'resp', 'sbp', 'dbp', 'map', 'EtCO2',
      'BaseExcess', 'HCO3', 'FiO2', 'pH', 'PaCO2', 'SaO2', 'AST', 'BUN',
      'Alkalinephos', 'Calcium', 'Chloride', 'Creatinine',
      'Glucose', 'Lactate', 'Magnesium', 'Phosphate', 'Potassium',
      'Bilirubin_total', 'Hct', 'Hgb', 'PTT', 'WBC',
      'Fibrinogen', 'Platelets']

#model 예시

def pred_sepsis(pred_sat:Record_for_Predict):
    # 랜덤한 0~100의 값을 가진 변수 생성
  percent = random.uniform(0, 100)
  
  # 실수값이 80 이상이면 1, 아니면 0을 리턴
  if percent >= 80:
      return 1,percent
  else:
      return 0,percent

# model predict
@router.get("/api/predict_sepsis/{pid}")
async def model_pred(pid:int):
  data_sat_raw2 = session.query(VitalRecordAllMask).filter(VitalRecordAllMask.pid == pid).order_by(VitalRecordAllMask.p_record_seq.desc()).limit(30).all()
  if data_sat_raw2:
    data_sat_raw = pd.DataFrame.from_records([record.__dict__ for record in data_sat_raw2])
    data_sat_raw.drop('_sa_instance_state',axis=1,inplace=True)
    data_sat_raw=data_sat_raw.sort_values(["pid", "p_record_seq"]).reset_index(drop=True)
    max_seq = len(data_sat_raw)
    max_ind = data_sat_raw.iloc[max_seq-1].ICULOS
    pred_sat=[]
    # ICULOS 값은 최근값만 사용하도록 해보자~
    for k in range(max_seq):
      if (data_sat_raw.iloc[max_seq-k-1].ICULOS - data_sat_raw.iloc[max_seq-k-2].ICULOS == 1):
        pred_sat.insert(0, data_sat_raw.iloc[max_seq-k-1])
      else:
        if k == max_seq-1:
          pred_sat.insert(0, data_sat_raw.iloc[max_seq-k-1])
          break
        else:
          break
    print(len(pred_sat))
    # 일단 최근 데이터 하나 가져와야 하네...
    latest_raw=session.query(VitalRecordAll).filter(VitalRecordAll.pid == pid).order_by(desc(VitalRecordAll.p_record_seq)).first()
    dict_latest_raw=latest_raw.__dict__
    df_latest=pd.DataFrame([dict_latest_raw]).copy()
    # pred_sat df로 묶어주기
    pred_sat=pd.DataFrame(pred_sat)
    # 스케일링하기~
    pred_list=[]
    for col in vital_cols:
      pred_sat[col] = (pred_sat[col] - mean_values[col]) / std_values[col]
    for i in range(len(pred_sat)):
      r = dict(pred_sat.iloc[i])
      pred_list.append(Record_for_Predict(**r))
    # update해주기
    sep,percent=pred_sepsis(pred_list)
    query=text("update vital_record_all set sepsis_in_six = :sepsis_in_six, sepsis_percent = :sepsis_percent where pid = :pid and p_record_seq = :p_record_seq")
    values={'sepsis_in_six' : sep,
            'sepsis_percent' : percent,
            'pid': pid,
            'p_record_seq':df_latest.iloc[0].p_record_seq}
    session.execute(query,values)
    session.commit()
    session.close()

@router.get("/api/data/")
async def get_data(limit: int = 10, page: int = 1):
  offset = (page - 1) * limit
  query = text(f"SELECT * FROM vital_record_now_view LIMIT :limit OFFSET :offset")
  result = session.execute(query, {"limit": limit, "offset": offset})
  data = [dict(row) for row in result]
  count = session.execute(text("SELECT COUNT(*) FROM vital_record_now_view")).fetchone()[0]
  session.close()
  return {"data": data, "count": count,'page':{'page':1,'limit':10}}

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
  query = text(f"UPDATE vital_record_all_mask SET hr = :hr, O2Sat = :O2Sat, temp = :temp, resp = :resp, sbp = :sbp, dbp = :dbp WHERE pid = :pid AND p_record_seq = :p_record_seq")
  values = {'hr': record_u.hr, 'O2Sat': record_u.O2Sat, 'temp': record_u.temp, 'resp': record_u.resp, 'sbp': record_u.sbp, 'dbp': record_u.dbp, 'pid': pid, 'p_record_seq': record_u.p_record_seq}
    # 쿼리 실행
  session.execute(query,values)
  session.commit()
  model_pred(pid)
  updated_record = session.query(AllPatientRecordView).filter(AllPatientRecordView.pid == pid, AllPatientRecordView.p_record_seq == record_u.p_record_seq).first()
  session.close()
  return updated_record

# 선택한 환자의 최근 7개 record를 가져오자
@router.get('/api/chart_records/{pid}')
async def chart_records(pid:int):
  
  query=text(f"SELECT * FROM all_patients_vital_record_view WHERE pid={pid} ORDER BY input_time DESC LIMIT 7")
  
  chart_records = session.execute(query).all()
  session.close()
  return chart_records

# lab data!!!!!!
@router.post('/api/lab_insert/{pid}')
async def lab_insert(pid:int,labdata: LabData):
    # -----------------lab_data_record 넣기--------------------------
  db_lab_data = LabDataRecord(**labdata.dict())
  session.add(db_lab_data)
  session.commit()

  # -----------------lab_data_filled 채우기-------------------
  df_fill_list = pd.read_sql(session.query(LabDataRecord).filter(LabDataRecord.pid==pid).statement, session.bind)
  # 채울때 하나채우고 dup을 해보자

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
  latest_raw = session.query(VitalRecordAll).filter_by(pid=pid).order_by(desc(VitalRecordAll.p_record_seq)).first()
  filled_raw = session.query(LabDataFilled).filter_by(pid=pid).order_by(desc(LabDataFilled.lab_record_seq)).first()
  if latest_raw:
    #------latest vital_record_all update)
    dict_latest_raw=latest_raw.__dict__
    dict_filled_raw=filled_raw.__dict__
    dict_latest=dict_latest_raw.copy()
    dict_filled=dict_filled_raw.copy()
    df_latest=pd.DataFrame([dict_latest])
    df_filled=pd.DataFrame([dict_filled])
    df_latest.drop('_sa_instance_state',axis=1,inplace=True)
    df_filled.drop('_sa_instance_state',axis=1,inplace=True)
    df_filled.drop('lab_record_seq',axis=1,inplace=True)
    # 이전 lab data는 빼주고 filled된걸로 합쳐서 업데이트해줄려고~~
    df_droped=df_latest.drop(lab_cols3,axis=1,inplace=False)
    # 이전 record_all 데이터와 새로운 lab_record 합쳐주기!
    df_merged=pd.merge(df_droped,df_filled,on='pid',how='outer')
    # to_dict!
    dict_merged=df_merged.iloc[0].to_dict()
    print(dict_merged)
    vital_update=VitalRecordAll(**dict_merged)
    session.merge(vital_update)
    session.commit()
    # latest_record가 있을 경우 vital_record_all 및 vital_record_all_mask 업데이트
    # COLS: 기존 column 이름들의 리스트
    MASK_COLS = [x+'_mask' for x in COLS]
    # 안되면 되는거해라
    data1 = session.execute(f"SELECT * FROM vital_record_all WHERE pid={pid} ORDER BY p_record_seq DESC").fetchone()
    cols = session.execute("SELECT column_name FROM information_schema.columns WHERE table_name='vital_record_all'").fetchall()
    cols = [c[0] for c in cols]  # 튜플을 리스트로 변환
    raw_data = pd.DataFrame([data1], columns=cols) # 데이터 프레임으로
    df_filled1 = raw_data.drop(['sepsis_in_six','sepsis_percent'],axis=1,inplace=False).copy()
    data2=raw_data.drop(lab_cols2,axis=1,inplace=False)
    data3=pd.DataFrame([labdata.dict()])
    # mask만들기위한 df
    df_sub=pd.merge(data2,data3,on='pid')
    df_masks = pd.DataFrame()
    for col in COLS:
        # 해당 column에서 NaN이 아닌 값의 index를 True로, NaN이면 False로 설정
        df_masks[col+'_mask'] = df_sub[col].isna().astype(int)
    # 모든 mask column을 결합하여 하나의 DataFrame으로 만듦
    df_masks = pd.concat([df_masks[x] for x in MASK_COLS], axis=1)
    df_filled1[df_masks.columns]=df_masks
    # df_filled와 df_masks를 merge
    df_sub_mask = df_filled1
    df_sub_dict=df_sub_mask.iloc[0].to_dict()

#   VitalRecordAllMask 테이블의 primary key가 'pid'와 'p_record_seq' 인지 확인이 필요합니다
# -------------vital_record_all_mask 업데이트~-----------------
    sub_mask = VitalRecordAllMask(**df_sub_dict)
    print(sub_mask)
    session.merge(sub_mask)
    session.commit()
  # # ------------------vital_record_all_mask 최근 batch 개 뽑아서 model pred 돌리기--------
  return pid
v_insert_list=['hr', 'O2Sat', 'temp', 'sbp', 'dbp', 'map', 'resp']
  # ------------------vital_record_all 최근 데이터 sepsis업데이트하기--------------
@router.post('/api/vital_insert/{pid}')
async def vital_insert(pid:int,vital: Record_i):
  input_time = datetime.datetime.strptime(vital.input_time, '%Y-%m-%dT%H:%M:%S')
  birth_date = datetime.datetime.strptime(vital.birth_date, '%Y-%m-%d').date()
    # -----------------vital_record_all 만들기 넣기--------------------------
  latest_filled=session.query(LabDataFilled).filter(LabDataFilled.pid==pid).order_by(desc(LabDataFilled.lab_record_seq)).first()
  vital_dict=vital.dict()

  if latest_filled: # lab data가 있을때
    filled_dict=latest_filled.__dict__
    filled_dict.pop('_sa_instance_state')
    df_vi=pd.DataFrame([vital_dict])
    pd_fi=pd.DataFrame([filled_dict])
    df_fi=pd_fi.drop(['lab_record_seq'],axis=1,inplace=False).copy()
    df_filled=pd.merge(df_vi,df_fi,on='pid',how='outer')
    merged_dict = df_filled.to_dict(orient='records')[0]
    df_vital_insult=VitalRecordAll(**merged_dict)
    session.add(df_vital_insult)
    session.commit()

  #-------------------vital_record_all_mask 만들어서 넣어주기-----------------
    mask_raw2=session.query(VitalRecordAllMask).filter(VitalRecordAllMask.pid==pid).order_by(desc(VitalRecordAllMask.p_record_seq)).first()
    dict_mask=mask_raw2.__dict__
    # merged_dict 재사용!
    df_mask=pd.DataFrame([dict_mask])
    df_mask_droped=df_mask.drop(COLS,axis=1,inplace=False)
    df_mask_droped.drop('_sa_instance_state',axis=1,inplace=True)
    df_merged_vital=pd.DataFrame([merged_dict]).copy()
    df_merged_vital.drop(['sepsis_in_six','sepsis_percent'],axis=1,inplace=True)
    df_vital_mask=pd.concat([df_merged_vital,df_mask_droped],axis=1)
    dict_vital_mask=df_vital_mask.to_dict('records')[0].copy()
    vital_mask_insert=VitalRecordAllMask(**dict_vital_mask)
    session.add(vital_mask_insert)
    session.commit()
    # model 예측 진행 및 예측값으로 업데이트
    await model_pred(pid)
  else:#lab data가 없을때~
      # -----------------vital_record_all 만들기 넣기--------------------------
    df_vi=pd.DataFrame([vital_dict])
    df_median=pd.DataFrame([mean_values])
    df_medi_droped=df_median.drop(v_insert_list,axis=1,inplace=False).copy()
    df_merged=pd.concat([df_vi,df_medi_droped],axis=1)
    merged_dict = df_merged.to_dict(orient='records')[0]
    vital_insert=VitalRecordAll(**merged_dict)
    session.add(vital_insert)
    session.commit()

    # ------------------vital_record_all_mask 만들기 넣기------------  ~~~~~~~~이부분도 모듈화가 가능할듯!!~~~~~~~~~~~~
    # 최근의 record_all 하나 가져오기
    latest_raw=session.query(VitalRecordAll).filter(VitalRecordAll.pid == pid).order_by(desc(VitalRecordAll.p_record_seq)).first()
    dict_latest_raw=latest_raw.__dict__
    df_latest=pd.DataFrame([dict_latest_raw])
    df_latest.drop('_sa_instance_state',axis=1,inplace=True)
    df_droped=df_latest.drop(lab_cols2,axis=1,inplace=False)

    # pid빼고 null으로 채워진 lab 데이터 생성!
    dict_null={'pid':pid}
    lab_null=LabData(**dict_null)
    dict_lab_null=lab_null.__dict__
    df_lab_null=pd.DataFrame([dict_lab_null])
    # merge data 생성해서 mask 만들어주기
    df_null_merged=pd.merge(df_droped,df_lab_null,on='pid',how='outer')
    df_masks = pd.DataFrame()
    MASK_COLS = [x+'_mask' for x in COLS]
    for col in COLS:
        # 해당 column에서 NaN이 아닌 값의 index를 True로, NaN이면 False로 설정
        df_masks[col+'_mask'] = df_null_merged[col].isna().astype(int)
    # 모든 mask column을 결합하여 하나의 DataFrame으로 만듦
    df_masks = pd.concat([df_masks[x] for x in MASK_COLS], axis=1)
    df_droped[df_masks.columns]=df_masks
    # df_filled와 df_masks를 merge
    df_null_merged_mask = df_droped
    df_null_merged_dict=df_null_merged_mask.iloc[0].to_dict()
#   VitalRecordAllMask 테이블의 primary key가 'pid'와 'p_record_seq' 인지 확인이 필요합니다
# -------------vital_record_all_mask 업데이트~-----------------
    sub_mask = VitalRecordAllMask(**df_null_merged_dict)
    session.add(sub_mask)
    session.commit()
    # 최근 30개만 사용!            ~~~~~~~이 아래부분은 모듈화가 가능할것같음!~~~~~~~~~~~~
    # model 예측 진행 및 예측값으로 업데이트
  return pid


