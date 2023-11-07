# app/main.py
from fastapi import FastAPI
from app.api.main import router as api_v1_router

app = FastAPI()

app.include_router(api_v1_router, prefix="/api")
