from enum import Enum
import uuid
from sqlalchemy import Column, Integer, String, UUID, DateTime, func
from datetime import UTC, datetime
from sqlmodel import Field, SQLModel


def get_datetime_utc() -> datetime:
    return datetime.now(UTC)


class StatusEnum(str, Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class PriorityEnum(str, Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"


class Admins(SQLModel, table=True):
    __tablename__ = "admins"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    login: str = Field(min_length=8, max_length=128)
    password: str = Field(min_length=8, max_length=128)


class Application(SQLModel, table=True):
    __tablename__ = "application"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(min_length=3, max_length=120)
    description: str | None = Field(max_length=1000)
    status: StatusEnum = Field(sa_column=Column(String))
    priority: PriorityEnum = Field(sa_column=Column(String))

    created_at: datetime = Field(
        default_factory=get_datetime_utc,
        sa_column_kwargs={
            "server_default": func.now(),
            "nullable": False
        },
        sa_type=DateTime(timezone=True)
        )

    updated_at: datetime = Field(
        default_factory=get_datetime_utc,
        sa_column_kwargs={
            "server_default": func.now(),
            "onupdate": func.now(),
            "nullable": False
        },
        sa_type=DateTime(timezone=True)
        )
