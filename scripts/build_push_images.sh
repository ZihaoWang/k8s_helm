#!/bin/bash

sudo docker login docker.io

DOCKER_HUB_USERNAME=evensong

sudo docker build -t $DOCKER_HUB_USERNAME/flask-app:latest -f src/app/Dockerfile .
sudo docker build -t $DOCKER_HUB_USERNAME/model-training:latest -f src/training/Dockerfile.train .

sudo docker push $DOCKER_HUB_USERNAME/flask-app:latest
sudo docker push $DOCKER_HUB_USERNAME/model-training:latest

