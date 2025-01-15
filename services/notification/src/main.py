from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Notification(BaseModel):
    recipient: str
    message: str

@app.post("/notify/")
def send_notification(notification: Notification):
    # Simuliert das Versenden einer Benachrichtigung
    return {"status": "sent", "recipient": notification.recipient, "message": notification.message}
