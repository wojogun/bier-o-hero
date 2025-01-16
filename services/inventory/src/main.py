import os
from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests

# Base configuration for Microservices
Base = declarative_base()

# Common database setup
POSTGRES_USER = os.getenv("POSTGRES_USER", "user")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "28hn/sdn$hsaj!JHJG/")
POSTGRES_DB = os.getenv("POSTGRES_DB", "inventory")
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@inventory-db.bierohero:5432/{POSTGRES_DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Inventory Table
class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    stock = Column(Integer)
    purchase_price = Column(Float, index=True)  # Einkaufspreis
    sale_price = Column(Float, index=True)      # Verkaufspreis

# Tabellen und Daten initialisieren
def initialize_database():
    with engine.connect() as connection:
        for command in INIT_SQL.split(";"):
            if command.strip():
                connection.execute(command)


# FastAPI app for Inventory Service
app = FastAPI()

@app.on_event("startup")
def startup():
    # Tabelle erstellen
    Base.metadata.create_all(bind=engine)
    # Default-Daten einfügen
    db = SessionLocal()
    try:
        if not db.query(Inventory).first():  # Nur hinzufügen, wenn die Tabelle leer ist
            default_data = [
                Inventory(product_name="Hirter Kellermeister", stock=50, purchase_price=2.5, sale_price=4.0),
                Inventory(product_name="Weitra Hell", stock=100, purchase_price=0.9, sale_price=1.3),
                Inventory(product_name="Mohrenbraeu Spezial", stock=25, purchase_price=0.8, sale_price=1.2),
                Inventory(product_name="Schremser Pils", stock=125, purchase_price=0.5, sale_price=1.0),
            ]
            db.add_all(default_data)
            db.commit()
            print("Default data inserted successfully.")
    except Exception as e:
        print(f"Error inserting default data: {e}")
    finally:
        db.close()

@app.get("/inventory/")
def read_inventory():
    db = SessionLocal()
    inventory_items = db.query(Inventory).all()
    db.close()
    return inventory_items

@app.post("/inventory/")
def update_inventory(product_name: str, stock_change: int):
    db = SessionLocal()
    inventory_item = db.query(Inventory).filter(Inventory.product_name == product_name).first()
    if inventory_item:
        inventory_item.stock += stock_change
        if inventory_item.stock < 20:
            trigger_restock_notification(product_name)
        db.commit()
        db.refresh(inventory_item)
        db.close()
        return inventory_item
    else:
        db.close()
        return {"error": "Product not found"}

def trigger_restock_notification(product_name):
    notification_service_url = "https://notification-service.bierohero/notify/"
    reorder_email = os.getenv("REORDER_EMAIL", "wolfi@cocheck.at")
    email_payload = {
        "recipient": reorder_email,
        "subject": "Nachbestellung",
        "message": f"Bitte 100 Stück von {product_name} Bier o'Hero liefern."
    }

    try:
        response = requests.post(notification_service_url, json=email_payload)
        response.raise_for_status()
    except Exception as e:
        print(f"Failed to send restock email via Notification Service: {e}")

if __name__ == "__main__":
    initialize_database()
    print("Run FastAPI application.")
