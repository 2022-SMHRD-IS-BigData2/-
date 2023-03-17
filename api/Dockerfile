FROM python:3.9

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 8002

COPY requirements.txt /code/requirements.txt

CMD ["uvicorn", "main:app","--host","0.0.0.0","--port","8002"]

