#!/bin/bash
flash run
#build ET lancer le conteneur
docker build -t FINANCE-IT .
docker run  --rm -v "$PWD:/srv/app" -p 8080:8080 financeit:latest
