from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@payment-db:5432/payment")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, index=True)
    amount = Column(Float)
    status = Column(String)

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.post("/payments/")
def process_payment(order_id: int, amount: float):
    db = SessionLocal()
    payment = Payment(order_id=order_id, amount=amount, status="completed")
    db.add(payment)
    db.commit()
    db.refresh(payment)
    db.close()
    return payment
