from fastapi import APIRouter, Depends,HTTPException, status,Request,Header
from fastapi.security import OAuth2PasswordBearer
from ..core.database import session
from ..core.pred_model import Sepsis_Pred_Model
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
import json
import torch
import torch.nn.functional as F
from ..core.security import check_token,token



pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
router = APIRouter()

col_stat = json.load(open('api\\col_stat.json', 'r'))
# vital_cols=['HR', 'O2Sat', 'Temp', 'SBP', 'DBP', 'MAP', 'Resp','EtCO2',
#       'BaseExcess', 'HCO3', 'FiO2', 'pH', 'PaCO2', 'SaO2', 'AST', 'BUN',
#       'Alkalinephos', 'Calcium', 'Chloride', 'Creatinine',
#       'Glucose', 'Lactate', 'Magnesium', 'Phosphate', 'Potassium',
#       'Bilirubin_total', 'Hct', 'Hgb', 'PTT', 'WBC',
#       'Fibrinogen', 'Platelets','Age']

# INFO_COLS = ['pid', 'HospAdmTime', 'ICULOS', 'SepsisLabel','Gender']

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

COLS = ['HR', 'O2Sat', 'Temp', 'SBP', 'MAP', 'DBP', 'Resp','EtCO2',
      'BaseExcess', 'HCO3', 'FiO2', 'pH', 'PaCO2', 'SaO2', 'AST', 'BUN',
      'Alkalinephos', 'Calcium', 'Chloride', 'Creatinine',
      'Glucose', 'Lactate', 'Magnesium', 'Phosphate', 'Potassium',
      'Bilirubin_total', 'Hct', 'Hgb', 'PTT', 'WBC',
      'Fibrinogen', 'Platelets','Age']

MASK_COLS = [x+"_mask" for x in COLS]
drop_list=["pid","p_record_seq","birth_date","input_time","Gender","ICULOS"]

#model 예시
def cut_or_fill_seq(input_tensor, seq_len=30):
  if input_tensor.shape[1]>seq_len:
      input_tensor=input_tensor[:,-seq_len:]
  elif input_tensor.shape[1]<seq_len:
      zeros = np.zeros([input_tensor.shape[0], seq_len-input_tensor.shape[1], input_tensor.shape[2]])
      input_tensor = np.concatenate([zeros, input_tensor], axis=1)
  return torch.Tensor(input_tensor)

def percent_80(output:float):
  if output>=0.8:
    sepsis=1
  else:
    sepsis=0
  return sepsis,output*100

sepsis_model=Sepsis_Pred_Model(66,64)
@router.post("/api/pred_test")
async def pred_test(list:List):
  nor_list=[]
  sep_list=[]
  for i in list:
    sep,pers=await model_pred(i)
    str=f"{i}환자 precent: {pers}, sep: {sep}"
    if pers>=80:
      sep_list.append(str)
    else:
      nor_list.append(str)
  print(sep_list)
  print(nor_list)
  return sep_list,len(sep_list), nor_list, len(nor_list)
  # import pdb; pdb.set_trace()
# model predict
@router.get("/api/predict_sepsis/{pid}")
async def model_pred(pid:int):
  data_sat_raw2 = session.query(VitalRecordAllMask).filter(VitalRecordAllMask.pid == pid).order_by(VitalRecordAllMask.p_record_seq.desc()).limit(30).all()
  if data_sat_raw2:
    data_sat_raw = pd.DataFrame.from_records([record.__dict__ for record in data_sat_raw2])
    data_sat_raw.drop('_sa_instance_state',axis=1,inplace=True)
    data_sat_raw=data_sat_raw.sort_values(["pid", "p_record_seq"]).reset_index(drop=True)
    max_seq = len(data_sat_raw)
    pred_sat=[]
    # ICULOS 값은 최근값만 사용하도록 해보자~
    for k in range(max_seq):
      if (data_sat_raw.iloc[max_seq-k-1].ICULOS - data_sat_raw.iloc[max_seq-k-2].ICULOS == 1):
        pred_sat.insert(0,data_sat_raw.iloc[max_seq-k-1])
      else:
        if k == max_seq-1:
          pred_sat.insert(0,data_sat_raw.iloc[max_seq-k-1])
          break
        else:
          break
    # pred_sat df로 묶어주기
    pred_sat2=pd.DataFrame(pred_sat)
    print(pred_sat2)
    pred_sat_dropped=pred_sat2.drop(drop_list,axis=1,inplace=False).copy()
    # 컬럼 재배열
    pred_sat_dropped = pred_sat_dropped[COLS+MASK_COLS]
    max_seq_len = 30
    # 스케일링하기~
    for col in COLS:
      pred_sat_dropped[col] = (pred_sat_dropped[col] - col_stat[col]['mean']) / col_stat[col]['std']
    # zero 패딩하기!
    pred_array=pred_sat_dropped.values
    # print(pred_array)
    input_tensor_raw = torch.tensor(pred_array, dtype=torch.float32).unsqueeze(0)
    input_tensor=cut_or_fill_seq(input_tensor_raw,seq_len=max_seq_len)

    sepsis_model.load_state_dict(torch.load("api\\0.775_2.pt"))
    sepsis_model.eval()
    with torch.no_grad():
      output_tensor = sepsis_model(input_tensor)
    # 출력값 출력
    output_tensor = F.sigmoid(output_tensor)
    output = output_tensor.squeeze().item() # Tensor에서 값을 꺼내서 scalar 값으로 변환
    # update해주기
    sep,percent=percent_80(output)
    query=text("update vital_record_all set sepsis_in_six = :sepsis_in_six, sepsis_percent = :sepsis_percent where pid = :pid and p_record_seq = :p_record_seq")
    values={'sepsis_in_six' : sep,
            'sepsis_percent' : percent,
            'pid': pid,
            'p_record_seq':data_sat_raw.iloc[-1].p_record_seq}
    session.execute(query,values)
    session.commit()
    session.close()
    return sep,percent

@router.get("/api/data/")
async def get_data(limit: int = 10, page: int = 1, token: str = Depends(check_token)):
  offset = (page - 1) * limit
  query = text(f"SELECT * FROM vital_record_now_view LIMIT :limit OFFSET :offset")
  result = session.execute(query, {"limit": limit, "offset": offset})
  data = [dict(row) for row in result]
  count = session.execute(text("SELECT COUNT(*) FROM vital_record_now_view")).fetchone()[0]
  session.close()
  return {"data": data, "count": count,'page':{'page':1,'limit':10}}

# 모든 환자의 최근 데이터에서 한명의 환자 선택
@router.get('/api/get_latest_all/{pid}')
async def get_latest_all(pid:int,token: str = Depends(check_token)):
  record=session.query(VitalRecordNowView).filter(VitalRecordNowView.pid==pid).all()
  session.close()
  return record

# sepsis 환자만 가져오기/페이징 들어갔음
@router.get('/api/get_latest_sepsis_all')
async def get_latest_sepsis_all(limit: int = 10, page: int = 1,token: str = Depends(check_token)):
  offset = (page - 1) * limit
  query = text(f"SELECT * FROM now_view_sepsis LIMIT :limit OFFSET :offset")
  result = session.execute(query, {"limit": limit, "offset": offset}).all()
  data = [dict(row) for row in result]
  count = session.execute(text("SELECT COUNT(*) FROM now_view_sepsis")).fetchone()[0]
  session.close()
  return {"data": data, "count": count,'page':{'page':1,'limit':10}}

# sepsis 위험확률 80프로 넘는것만 / 페이징 들어갔음
@router.get('/api/get_latest_sepsis_percent')
async def get_latest_sepsis_percent(limit: int = 10, page: int = 1,token: str = Depends(check_token)):
  offset = (page - 1) * limit
  query = text(f"SELECT * FROM vital_record_now_view where sepsis_percent>=80 LIMIT :limit OFFSET :offset")
  result = session.execute(query, {"limit": limit, "offset": offset}).all()
  data = [dict(row) for row in result]
  count = session.execute(text("SELECT COUNT(*) FROM vital_record_now_view where sepsis_percent>=80")).fetchone()[0]
  session.close()
  return {"data": data, "count": count,'page':{'page':1,'limit':10}}

#
@router.get('/api/get_all_record')
async def get_all_record(token: str = Depends(check_token)):
  record=session.query(AllPatientRecordView).all()
  session.close()
  return record

@router.get('/api/get_select_date')
async def get_select_date(pid:int,date:str,token: str = Depends(check_token)):
  date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()  # 문자열 형식의 날짜를 datetime 객체로 변환
  record = session.query(AllPatientRecordView).filter(and_(AllPatientRecordView.pid == pid, AllPatientRecordView.input_time >= date_obj, AllPatientRecordView.input_time < date_obj + datetime.timedelta(days=1))).all()
  session.close()
  return record

# 검색기능~페이지 추가하면 딕셔너리부분에 추가해주면됨
@router.get('/api/get_search_data')
async def get_search_patient(path: str = '', search_str: str = '', limit: int = 10, page: int = 1,token: str = Depends(check_token)):
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
async def get_select_record(pid: int, input_time: str,token: str = Depends(check_token)):
    input_time = datetime.datetime.strptime(input_time, '%Y-%m-%dT%H:%M:%S')
    query = text(f'select * from all_patients_vital_record_view where pid =:pid and input_time=:input_time')
    record = session.execute(query, {"pid":pid,"input_time": input_time}).first()
    session.close()
    return {"data": record}

# record 수정한 값 받아서 업데이트하는 api
@router.post('/api/update_record/{pid}')
async def update_record(pid:int, record_u:Record_u,token: str = Depends(check_token)):
  query = text(f"UPDATE vital_record_all SET HR = :HR, O2Sat = :O2Sat, Temp = :Temp, Resp = :Resp, SBP = :SBP, DBP = :DBP WHERE pid = :pid AND p_record_seq = :p_record_seq")
  values = {'HR': record_u.HR, 'O2Sat': record_u.O2Sat, 'Temp': record_u.Temp, 'Resp': record_u.Resp, 'SBP': record_u.SBP, 'DBP': record_u.DBP, 'pid': pid, 'p_record_seq': record_u.p_record_seq}
    # 쿼리 실행
  session.execute(query,values)
  session.commit()
  query = text(f"UPDATE vital_record_all_mask SET HR = :HR, O2Sat = :O2Sat, Temp = :Temp, Resp = :Resp, SBP = :SBP, DBP = :DBP WHERE pid = :pid AND p_record_seq = :p_record_seq")
  values = {'HR': record_u.HR, 'O2Sat': record_u.O2Sat, 'Temp': record_u.Temp, 'Resp': record_u.Resp, 'SBP': record_u.SBP, 'DBP': record_u.DBP, 'pid': pid, 'p_record_seq': record_u.p_record_seq}
    # 쿼리 실행
  session.execute(query,values)
  session.commit()
  model_pred(pid)
  updated_record = session.query(AllPatientRecordView).filter(AllPatientRecordView.pid == pid, AllPatientRecordView.p_record_seq == record_u.p_record_seq).first()
  session.close()
  return updated_record

# 선택한 환자의 최근 7개 record를 가져오자
@router.get('/api/chart_records/{pid}')
async def chart_records(pid:int,token: str = Depends(check_token)):
  query=text(f"SELECT * FROM all_patients_vital_record_view WHERE pid={pid} ORDER BY input_time DESC LIMIT 7")

  chart_records = session.execute(query).all()
  session.close()
  return chart_records

# lab data!!!!!!
@router.post('/api/lab_insert/{pid}')
async def lab_insert(pid:int,labdata: LabData,token: str = Depends(check_token)):
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
    df_fill_list.loc[first_index, col] = df_fill_list.loc[first_index,col].apply(lambda x:col_stat[col]['median'] if pd.isna(x) else x)
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
    vital_update=VitalRecordAll(**dict_merged)
    session.merge(vital_update)
    session.commit()
    # latest_record가 있을 경우 vital_record_all 및 vital_record_all_mask 업데이트
    # COLS: 기존 column 이름들의 리스트
    # 안되면 되는거해라
    data1 = session.execute(f"SELECT * FROM vital_record_all WHERE pid={pid} ORDER BY p_record_seq DESC").fetchone()
    raw_data = pd.DataFrame([data1]) # 데이터 프레임으로
    df_filled1 = raw_data.drop(['sepsis_in_six','sepsis_percent'],axis=1,inplace=False).copy()
    data2=raw_data.drop(lab_cols2,axis=1,inplace=False)
    data3=pd.DataFrame([labdata.dict()])
    # mask만들기위한 df
    df_sub=pd.merge(data2,data3,on='pid')
    df_masks = pd.DataFrame()
    for col in COLS:
        # 해당 column에서 NaN이 아닌 값의 index를 True로, NaN이면 False로 설정
        df_masks[col+'_mask'] = df_sub[col].notnull().astype(int)
    # 모든 mask column을 결합하여 하나의 DataFrame으로 만듦
    df_masks = pd.concat([df_masks[x] for x in MASK_COLS], axis=1)
    df_filled1[df_masks.columns]=df_masks
    # df_filled와 df_masks를 merge
    df_sub_mask = df_filled1.copy()
    df_sub_dict=df_sub_mask.iloc[0].to_dict()
    print(df_sub_dict)
#   VitalRecordAllMask 테이블의 primary key가 'pid'와 'p_record_seq' 인지 확인이 필요합니다
# -------------vital_record_all_mask 업데이트~-----------------
    sub_mask = VitalRecordAllMask(**df_sub_dict)
    session.merge(sub_mask)
    session.commit()
#   # # ------------------vital_record_all_mask 최근 batch 개 뽑아서 model pred 돌리기--------
  return pid

v_insert_list=['HR', 'O2Sat', 'Temp', 'SBP', 'DBP', 'MAP', 'Resp']

  # ------------------vital_record_all 최근 데이터 sepsis업데이트하기--------------
@router.post('/api/vital_insert/{pid}')
async def vital_insert(pid:int,vital: Record_i,token: str = Depends(check_token)):
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
  else:#lab data가 없을때~
    vital_dict=vital.dict()
    df_vi=pd.DataFrame([vital_dict])
    lab_list=[]
    for col in COLS:
      lab_list.append([col_stat[col]['median']])  # [] 추가
    df_median=pd.DataFrame(lab_list).T
    df_median.columns=COLS
    df_medi_droped=df_median.drop(v_insert_list,axis=1,inplace=False).copy()
    df_merged=pd.concat([df_vi,df_medi_droped],axis=1)
    merged_dict = df_merged.to_dict(orient='records')[0]
    vital_insert=VitalRecordAll(**merged_dict)
    print(merged_dict)
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
        df_masks[col+'_mask'] = df_null_merged[col].notnull().astype(int)
    # 모든 mask column을 결합하여 하나의 DataFrame으로 만듦
    df_masks = pd.concat([df_masks[x] for x in MASK_COLS], axis=1)
    df_droped[df_masks.columns]=df_masks
    # df_filled와 df_masks를 merge
    df_null_merged_mask2 = pd.merge(df_latest,df_droped)
    df_null_merged_mask=df_null_merged_mask2.drop(['sepsis_in_six','sepsis_percent'],axis=1,inplace=False).copy()
    df_null_merged_dict=df_null_merged_mask.iloc[0].to_dict()
    print(df_null_merged_dict)

  # # -------------vital_record_all_mask 업데이트~-----------------
    sub_mask = VitalRecordAllMask(**df_null_merged_dict)
    session.add(sub_mask)
    session.commit()
  return pid



@router.post('/api/vital_insert_initial/{pid}')
async def vital_insert(pid:int,vital: Record_i,token: str = Depends(check_token)):
      # -----------------vital_record_all 만들기 넣기--------------------------
  vital_dict=vital.dict()
  df_vi=pd.DataFrame([vital_dict])
  lab_list=[]
  for col in COLS:
    lab_list.append([col_stat[col]['median']])  # [] 추가
  df_median=pd.DataFrame(lab_list).T
  df_median.columns=COLS
  df_medi_droped=df_median.drop(v_insert_list,axis=1,inplace=False).copy()
  df_merged=pd.concat([df_vi,df_medi_droped],axis=1)
  merged_dict = df_merged.to_dict(orient='records')[0]
  vital_insert=VitalRecordAll(**merged_dict)
  print(merged_dict)
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
      df_masks[col+'_mask'] = df_null_merged[col].notnull().astype(int)
  # 모든 mask column을 결합하여 하나의 DataFrame으로 만듦
  df_masks = pd.concat([df_masks[x] for x in MASK_COLS], axis=1)
  df_droped[df_masks.columns]=df_masks
  # df_filled와 df_masks를 merge
  df_null_merged_mask2 = pd.merge(df_latest,df_droped)
  df_null_merged_mask=df_null_merged_mask2.drop(['sepsis_in_six','sepsis_percent'],axis=1,inplace=False).copy()
  df_null_merged_dict=df_null_merged_mask.iloc[0].to_dict()
  print(df_null_merged_dict)

# # -------------vital_record_all_mask 업데이트~-----------------
  sub_mask = VitalRecordAllMask(**df_null_merged_dict)
  session.add(sub_mask)
  session.commit()
  return pid


@router.get("/api/sepsis_list_for_alarm")
async def sepsis_list_for_alarm():
  sepsis_raw = session.query(NowViewSepsis).all()
  sepsis_list = [{"pid": x.pid, "name": x.name} for x in sepsis_raw]

  return  {"name_list":sepsis_list}
