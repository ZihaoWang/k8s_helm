# Flask ML App Deployment

This document provides a step-by-step guide to containerize and deploy a Flask-based machine learning application using Docker, Kubernetes (Minikube), and Helm.

# Prerequisites

* Docker
* Docker Hub account
* Minikube
* Helm

# Directory Structure

```
assignment/
├── src/
│   ├── app/
│   │   └── main.py
│   ├── data/
│   │   └── diabetes.csv
│   ├── models/
│   │   └── trained models will be saved here
│   └── training/
│       └── train.py
├── Dockerfile
├── Dockerfile.train
├── requirements.txt
├── k8s/
│   ├── flask-app-deployment.yaml
│   ├── flask-app-service.yaml
│   ├── model-training-job.yaml
│   ├── model-training-cronjob.yaml
├── helm-chart/
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
│       ├── deployment.yaml
│       ├── service.yaml
│       └── cronjob.yaml
├── scripts/
│   ├── build_push_images.sh
│   └── deploy.sh
└── README.md
```

# Step-by-Step Guide

1. Build and Push Docker Images

Dockerfile for Flask App (assignment/Dockerfile)

```
cd assignment
./scripts/build_push_images.sh
```

2. Start Minikube

Start Minikube to create a local Kubernetes cluster.

```
minikube start
```

3. Deploy Using Helm

```
./scripts/deploy.sh
```

4. Access the Flask App

Get the Minikube IP address and access the Flask app.

```
minikube ip
```

Access the Flask app via http://<minikube-ip>:30001.

5. Verify Model Training CronJob

Check the status of the CronJob and view logs to verify it runs every 5 minutes.

```
# Check the status of the CronJob
kubectl get cronjobs

# Check the logs of a job run
kubectl logs job/model-training-cronjob-<job-id>
```
