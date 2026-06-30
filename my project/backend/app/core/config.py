from sqlalchemy import create_engine
# from pydantic_settings import BaseSettings


SQLALCHEMY_DATABASE_URL = 

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

class Settings(BaseSettings):
