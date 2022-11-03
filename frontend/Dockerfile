FROM node:16-slim

RUN useradd --create-home --home-dir /app --shell /bin/bash app
WORKDIR /app

COPY package*.json ./
RUN npm i

COPY . .
USER app
