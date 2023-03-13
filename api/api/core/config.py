from pydantic import BaseSettings

user_name = 'sepsis'
user_pwd = 'sepsis'
db_host = 'project-db-stu2.ddns.net'
db_name = 'sepsis'


class Settings(BaseSettings):
    PROJECT_NAME: str = "sepsis"
    PROJECT_DESCRIPTION: str = "sepsis"
    API_V1_STR: str = "/api/v1"
    database :str= 'mysql://%s:%s@%s:3308/%s' % (
                    user_name,
                    user_pwd,
                    db_host,
                    db_name
)

settings = Settings()