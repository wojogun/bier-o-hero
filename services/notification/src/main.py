import os
from fastapi import FastAPI
from pydantic import BaseModel
import smtplib

# FastAPI app for Notification Service
app = FastAPI()

# Email configuration (replace with real SMTP settings)
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER", "your-email@example.com")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "your-password")

POSTGRES_USER = os.getenv("POSTGRES_USER", "user")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "28hn/sdn$hsaj!JHJG/")
POSTGRES_DB = os.getenv("POSTGRES_DB", "notification")
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@notification-db.bierohero:5432/{POSTGRES_DB}"


# Email payload model
class EmailPayload(BaseModel):
    recipient: str
    subject: str
    message: str

@app.post("/notify/")
def send_email(payload: EmailPayload):
    try:
        # Establish connection to SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)

            # Create email message
            email_text = f"Subject: {payload.subject}\n\n{payload.message}"

            # Send email
            server.sendmail(SMTP_USER, payload.recipient, email_text)

        return {"status": "success", "message": "Email sent successfully."}
    except Exception as e:
        print(f"Failed to send email: {e}")
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    print("Notification Service is running.")
