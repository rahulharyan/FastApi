from fastapi import FastAPI
from app.core.database import engine,Base
from app.models import user,todo

Base.metadata.create_all(bind=engine)

app=FastAPI(title="Todo Application")