import os
from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base configuration for Microservices
Base = declarative_base()

# Common database setup
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./inventory.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Inventory model
class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    stock = Column(Integer)

# FastAPI app for Inventory Service
app = FastAPI()

@app.on_event("startup")
def startup():
    # Create tables on startup
    Base.metadata.create_all(bind=engine)

@app.get("/inventory/")
def read_inventory():
    db = SessionLocal()
    inventory_items = db.query(Inventory).all()
    db.close()
    return inventory_items

@app.post("/inventory/")
def create_inventory_item(product_name: str, stock: int):
    db = SessionLocal()
    new_item = Inventory(product_name=product_name, stock=stock)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    db.close()
    return new_item

@app.put("/inventory/{item_id}/")
def update_inventory_item(item_id: int, stock: int):
    db = SessionLocal()
    item = db.query(Inventory).filter(Inventory.id == item_id).first()
    if item:
        item.stock = stock
        db.commit()
        db.refresh(item)
    db.close()
    return item

@app.delete("/inventory/{item_id}/")
def delete_inventory_item(item_id: int):
    db = SessionLocal()
    item = db.query(Inventory).filter(Inventory.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
    db.close()
    return {"message": "Item deleted successfully"}
