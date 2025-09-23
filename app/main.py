from fastapi import FastAPI
from app.api.weather import router as weather_router
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
import random


app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

app.include_router(weather_router, prefix="/weather", tags=["weather"])

@app.get("/")
def read_root(request: Request):
    # return {"message": "Welcome to the Weather API Wrapper"}
    return templates.TemplateResponse("index.html", {"request": request})
