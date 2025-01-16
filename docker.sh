#!/bin/bash
docker build ./services/event/ -t wojogu/mcce24-secpv-event-service:1.0
docker build ./services/inventory -t wojogu/mcce24-secpv-inventory-service:1.0
docker build ./services/notification -t wojogu/mcce24-secpv-notification-service:1.0
docker build ./services/order -t wojogu/mcce24-secpv-order-service:1.1
docker build ./services/payment -t wojogu/mcce24-secpv-payment-service:1.0

docker build ./frontend -t wojogu/mcce24-secpv-frontend:1.0