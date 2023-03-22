# Python 이미지를 기반으로 작성
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /api

# requirements.txt 파일을 이미지에 복사
COPY requirements.txt .

# requirements.txt에 나열된 라이브러리를 설치
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드를 이미지에 복사
COPY . .

# Uvicorn을 사용하여 FastAPI 애플리케이션 실행 (포트 및 호스트 옵션에 따라 조정)
CMD ["uvicorn", "main:app", "--port", "8002"]

# 실행 명령어
# docker build -t your_image_name .
