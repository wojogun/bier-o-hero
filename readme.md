# Bier o'Hero
Das ultimative Bier-Bestell-Tool

## Voraussetzungen
- Windows 11
- Ranger Desktop
- wsl

## Installation 
Die Docker-Images sind auf hub.docker.com öffentlich verfügbar und werden von Kubernates heruntergeladen.
In der WSL oder sonstigen Linux-Shell dann die Datei run ausführen. Diese Datei macht nichts anderes, als alle apply-Befehle auszuführen

```
kubectl apply -f k8s/namespace.yaml
kubectl create secret tls all-tls   --cert=nogit/cert.pem   --key=nogit/key.pem   -n bierohero
kubectl apply -f k8s/secrets.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/order-service.yaml
kubectl apply -f k8s/inventory-service.yaml
kubectl apply -f k8s/notification-service.yaml
kubectl apply -f k8s/payment-service.yaml
kubectl apply -f k8s/event-service.yaml
kubectl apply -f k8s/frontend-service.yaml
```
 
Die Webseite ist dann auf http://localhost:8080

## Anmerkungen
Es ist eine Demo! Daher folgende Punkte zur Beachtung:
- Die Zertifikate und Secrets sollten in einer produktiven Umgebung selbstverständlich nicht im Repo aufscheinen.
- Kein Artdirektor segnet dieses Layout ab 😉
- Status ist bestensfalls Alpha.
- Wir sind für jedes Zusatzpünktchen dankbar.
- Dateien sind nicht optimiert. Es kann also recht viel Schrott im Repo sein.