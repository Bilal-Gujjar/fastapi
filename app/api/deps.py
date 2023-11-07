from sqlalchemy.orm import Session
from fastapi import Depends
from ecommerce_manager.app.core.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
