# Basis-Image
FROM python:3.9-slim

# Setze das Arbeitsverzeichnis
WORKDIR /app

# Kopiere die Abhängigkeiten und installiere sie
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Code
COPY . .

# Exponiere den Port
EXPOSE 8000

# Startbefehl
CMD ["uvicorn", "order_service:app", "--host", "0.0.0.0", "--port", "8000"]
