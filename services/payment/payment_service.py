from fastapi import FastAPI
from sqlalchemy import Column, Integer, String, Float
from database import Base, engine, SessionLocal

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer)
    status = Column(String)
    amount = Column(Float)

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/payments/")
def process_payment(order_id: int, amount: float):
    db = SessionLocal()
    payment = Payment(order_id=order_id, status="completed", amount=amount)
    db.add(payment)
    db.commit()
    db.refresh(payment)
    db.close()
    return payment
