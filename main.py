from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles   #<-- Add this

app = FastAPI()


#static files & load
app.mount("/", StaticFiles(directory="static", html = True), name="static") #<-- Add this