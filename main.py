from fastapi import FastAPI, File, UploadFile, Request
from fastapi.staticfiles import StaticFiles   #<-- Add this
import mariadb
from fastapi.responses import FileResponse

app = FastAPI()

#static files & load
app.mount("/", StaticFiles(directory="static", html = True), name="static") #<-- Add this

@app.get("*")
async def web(request: Request):
    return FileResponse('static/index.html',media_type='text/html')