from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

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
