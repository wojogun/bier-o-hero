import os
from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base configuration for Microservices
Base = declarative_base()

# Common database setup
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Example for Order Service
class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, index=True)
    product_name = Column(String, index=True)
    quantity = Column(Integer)
    total_price = Column(Float)

# FastAPI app for Order Service
app = FastAPI()

@app.on_event("startup")
def startup():
    # Create tables on startup
    Base.metadata.create_all(bind=engine)

@app.get("/orders/")
def read_orders():
    db = SessionLocal()
    orders = db.query(Order).all()
    db.close()
    return orders

@app.post("/orders/")
def create_order(customer_name: str, product_name: str, quantity: int, total_price: float):
    db = SessionLocal()
    new_order = Order(
        customer_name=customer_name,
        product_name=product_name,
        quantity=quantity,
        total_price=total_price,
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    db.close()
    return new_order

# Example Frontend Interaction Placeholder
def frontend_placeholder():
    print("Frontend React.js interacting with APIs")

if __name__ == "__main__":
    print("Run FastAPI application.")
