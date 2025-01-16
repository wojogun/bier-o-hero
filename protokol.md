# Bier o'Hero
Das ultimative Bier-Bestell-Tool

## Voraussetzungen
- Windows 11
- Ranger Desktop
- wsl
```
wsl --install
``` 
-  python3 mit pip
```
sudo apt install python3 python3-pip -y
```
prüfen, ob alles passt:
```
python3 --version
pip3 --version
```
- virtuelle Umgebung einrichten
```
sudo apt install python3-venv -y
python3 -m venv env
```
- Pakete in der virtuellen Umgebung installieren
```
pip3 install fastapi uvicorn sqlalchemy
pip install psycopg2-binary
cd bier_o_hero/services
source ../env/bin/activate
```
starten des scripts:
```
uvicorn order_service:app --reload
```
swagger testen:  
http://127.0.0.1:8000/docs.

```
```


## Installation 



## Postgres
```
psql -U user -d postgres  
\l # zeigt dbs
\c name #wechselt zur db
```