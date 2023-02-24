from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import mysql
# user_name = 'sepsis'
# user_pwd = 'sepsis'
# db_host = ''
# db_name = 'sepsis'


user_name = 'sepsis'
user_pwd = 'sepsis'
db_host = 'project-db-stu2.ddns.net'
db_name = 'sepsis'

database = 'mysql://%s:%s@%s:3307/%s' % (
  user_name,
  user_pwd,
  db_host,
  db_name
)
# DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

ENGINE = create_engine(
  database,
  echo=True
)

session = scoped_session(
  sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=ENGINE
  )
)

Base = declarative_base()
Base.query = session.query_property()


# 전통적인 방법을 사용한 db 연결 객체 만들기

import mysql.connector
from fastapi import FastAPI, Depends,Response
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.pool import QueuePool
from sqlalchemy import create_engine, MetaData

class Database:
    def __init__(self, app: FastAPI):
        self.app = app
        self.pool = None

    def connect(self):
        # 데이터베이스 연결 설정
        db_config = {
          "host": "project-db-stu2.ddns.net",
          "user": "sepsis",
          "password": "sepsis",
          "database": "sepsis",
          "port" : 3307
      }

        # 커넥션 풀 설정
        self.pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **db_config)

    def execute(self, query):
        connection = self.pool.get_connection()
        cursor = connection.cursor(buffered=True, dictionary=True)

        cursor.execute(query)
        results = cursor.fetchall() if cursor else None

        cursor.close()
        connection.close()

        return results
