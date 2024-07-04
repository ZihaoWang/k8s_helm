# Flask ML App Deployment

This document provides a step-by-step guide to containerize and deploy a Flask-based machine learning application using Docker, Kubernetes (Minikube), and Helm.

The following settings are implemented:

* Two different Docker containers for app.py and training.py.
* A Cronjob of training.py for each 5 minutes.
* A Kubernetes Job of training.py before the deployment of APP, to prevent error caused by nonexist of trained model before the first Cronjob.
* Regular health (readness and liveness) check of the APP.

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
│   │   ├── main.py
│   │   └── Dockerfile
│   ├── data/
│   │   └── diabetes.csv
│   ├── models/
│   │   └── (the trained models will be saved here)
│   └── training/
│       ├── train.py
│       └── Dockerfile.train
├── requirements.txt
├── helm-chart/
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
│       ├── deployment.yaml
│       ├── service.yaml
│       └── cronjob.yaml
│       ├── job_init_hook.yaml
│       ├── pv.yaml
│       └── pvc.yaml
├── scripts/
│   ├── build_push_images.sh
│   └── deploy.sh
└── README.md
```

# Step-by-Step Guide

1. Build and push Docker images for the Flask APP and the training script.

```
cd assignment
./scripts/build_push_images.sh
```

2. Start a local Kubernetes cluster using Minikube.

```
minikube start
```

3. Deploy the application to the Kubernetes cluster using Helm..

```
./scripts/deploy.sh
```

4. Access the Flask App

Forward a port from a Kubernetes service to a local machine, allowing us to access the service locally for testing or other purposes.
```
kubectl port-forward --address 0.0.0.0 -n default service/flask-ml-app 30001:80
```

Then, we can access the Flask APP via http://localhost:30001/predictions,
```
curl localhost:30001/predictions
```
or check the health of our APP:
```
curl localhost:30001/health
```

We can also check the status of our Cronjob.
```
kubectl get cronjobs
```

5. Undeploy the Flask APP
```
./scripts/undeploy.sh
```

# Purpose of scripts

* scripts/build\_push\_images.sh
    - Script to build and push Docker images for the Flask app and the training script to Docker Hub.

* scripts/deploy.sh
    - Script to deploy the application using Helm.

* scripts/undeploy.sh
    - Script to undeploy the application using Helm.

# Purpose of Manifests and Charts

* helm-chart/Chart.yaml

    - Metadata for the Helm chart, including name, description, and version.

* helm-chart/values.yaml

    - Default values for the Helm chart, such as image repository, tag, service configuration, and cronjob schedule.

* helm-chart/templates/deployment.yaml
    - Kubernetes Deployment manifest template for the Flask app. It specifies the number of replicas, container image, ports, health checks, liveness checks and volumes.

* helm-chart/templates/service.yaml
    - Kubernetes Service manifest template for exposing the Flask app.

* helm-chart/templates/cronjob.yaml
    - Kubernetes CronJob manifest template for running the training script at scheduled intervals.

* helm-chart/templates/job\_init\_hook.yaml
    - A Kubernetes Job manifest template for initializing a training task before the APP starts.

* helm-chart/templates/pv.yaml
    - Kubernetes PersistentVolume (PV) manifest template. It defines the storage available to the cluster, which can be used by PersistentVolumeClaims (PVCs).

* helm-chart/templates/pvc.yaml
    - Kubernetes PersistentVolumeClaim (PVC) manifest template. It requests storage resources defined by a PersistentVolume (PV), ensuring data persists across pod restarts.

