# Sepsis

-------------------fastapi-------------------------------
fastapi 실행법
터미널 실행 후 아래 코드 입력
pip install pydantic
pip install sqlalchemy
pip install starlette
pip install uvicorn
pip install fastapi // 업데이트하라고하면 업데이트 코드 복붙 하세요
cd api
pwd 확인 : C:\Users\smhrd\sepsis_fastapi\Sepsis\api
다음 uvicorn 으로 fastapi 실행
uvicorn main:app --reload
혹은
uvicorn main:app --reload --host=172.30.1.(25 자기꺼) --port=(8807 자기꺼)
실행된 인터넷 창에서 주소창뒤에 /docs 입력후 엔터 > 원하는 자료 트라이
--------------------------------------------------------------------------