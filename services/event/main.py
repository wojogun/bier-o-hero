from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@event-db:5432/event")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.post("/events/")
def create_event(name: str, description: str):
    db = SessionLocal()
    new_event = Event(name=name, description=description)
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    db.close()
    return new_event
