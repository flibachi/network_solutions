# scripts/create_test_data.py
import os
import sys
from pathlib import Path

# Добавляем корень проекта в PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from sqlmodel import Session, create_engine
from models import Application, status, priority

load_dotenv()

def create_test_application():
    database_url = os.getenv("SQLMODEL_DATABASE_URL")
    engine = create_engine(
        database_url, 
        connect_args={"check_same_thread": False},
        echo=True
    )

    with Session(engine) as session:
        application_1 = Application(
            title="Тестовое название",
            description="Тестовое описание",
            status=status.NEW,
            priority=priority.NORMAL
        )
        session.add(application_1)
        session.commit()
        
        print(f"✓ Создана заявка:")
        print(f"  ID: {application_1.id}")
        print(f"  Title: {application_1.title}")
        print(f"  Created: {application_1.created_at}")
        print(f"  Updated: {application_1.updated_at}")

if __name__ == "__main__":
    create_test_application()