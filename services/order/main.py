import os
from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import requests

# Base configuration for Microservices
Base = declarative_base()

# Common database setup
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Orders Table
class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, index=True, unique=True)
    customer_name = Column(String, index=True)
    customer_email = Column(String, index=True)
    customer_address = Column(String, index=True)
    customer_zipcode = Column(String, index=True)
    customer_city = Column(String, index=True)
    contents = relationship("OrderContent", back_populates="order")

# OrderContent Table
class OrderContent(Base):
    __tablename__ = "ordercontent"
    content_id = Column(Integer, primary_key=True, index=True, unique=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    product_name = Column(String, index=True)
    sale_price = Column(Float, index=True)
    quantity = Column(Integer, index=True)
    order = relationship("Order", back_populates="contents")

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
def create_order(customer_name: str, customer_email: str, customer_address: str, customer_zipcode: str, customer_city: str, contents: list[dict]):
    db = SessionLocal()
    new_order = Order(
        customer_name=customer_name,
        customer_email=customer_email,
        customer_address=customer_address,
        customer_zipcode=customer_zipcode,
        customer_city=customer_city,
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    for content in contents:
        new_content = OrderContent(
            order_id=new_order.order_id,
            product_name=content["product_name"],
            sale_price=content["sale_price"],
            quantity=content["quantity"],
        )
        db.add(new_content)
    db.commit()

    # Send confirmation email via Notification Service
    send_confirmation_email_via_service(new_order, contents)

    db.close()
    return new_order

def send_confirmation_email_via_service(order, contents):
    notification_service_url = "https://notification-service.bierohero/notify/"
    email_body = f"Hallo {order.customer_name},\n\n" \
                 f"wir haben Deine Bestellung erhalten. Folgende Artikel werden Dir bald zugestellt:\n\n"
    for content in contents:
        email_body += f"- {content['product_name']} (Menge: {content['quantity']})\n"

    email_payload = {
        "recipient": order.customer_email,
        "subject": f"Order-ID {order.order_id} - Wir bestätigen Ihre Bestellung.",
        "message": email_body
    }

    try:
        response = requests.post(notification_service_url, json=email_payload)
        response.raise_for_status()
    except Exception as e:
        print(f"Failed to send email via Notification Service: {e}")

if __name__ == "__main__":
    print("Run FastAPI application.")
