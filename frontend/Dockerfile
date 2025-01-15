# Basis-Image für Node.js
FROM node:18-alpine as build

# Arbeitsverzeichnis setzen
WORKDIR /app

# Abhängigkeiten kopieren und installieren
COPY package.json package-lock.json ./
RUN npm install

# Quellcode kopieren und Build erstellen
COPY . ./

ENV NODE_OPTIONS=--openssl-legacy-provider
RUN npm run build

# Bereitstellungsphase: NGINX verwenden
FROM nginx:stable-alpine

# Kopiere den Build-Output nach NGINX
COPY --from=build /app/build /usr/share/nginx/html

# Exponiere Port 80 für den Service
EXPOSE 80

# Starten Sie NGINX
CMD ["nginx", "-g", "daemon off;"]
