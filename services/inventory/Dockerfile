FROM python:3.9-slim

# Installiere systemabhängige Pakete
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

# initiale Daten
# COPY init.sql /docker-entrypoint-initdb.d/

# Setze das Arbeitsverzeichnis
WORKDIR /app

# Kopiere die Abhängigkeiten und installiere sie
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Kopiere den Anwendungscode
COPY src/ .

# Exponiere den Port
EXPOSE 8000

# Starte den Service
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]