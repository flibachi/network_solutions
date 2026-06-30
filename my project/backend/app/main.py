import os
from fastapi import FastAPI
from dotenv import load_dotenv
from sqlmodel import SQLModel, Session, create_engine
from models import Application, StatusEnum, PriorityEnum
# from sqlalchemy import create_engine
# from models import Base, Application

load_dotenv()

database_url = os.getenv("SQLMODEL_DATABASE_URL")

engine = create_engine(
    database_url, connect_args={"check_same_thread": False}
)

SQLModel.metadata.create_all(engine)

with Session(engine) as session:

    application_1 = Application(
        title="Тестовое название",
        description="Тестовое описание",
        status=StatusEnum.NEW,
        priority=PriorityEnum.NORMAL)

    session.add(application_1)
    session.commit()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World!"}
