Robot Operations Platform

A cloud-native Robot Operations Platform built to manage robot fleet data, simulate robot activity, and monitor infrastructure through a complete DevOps workflow.

The project demonstrates containerization, CI/CD automation, Kubernetes orchestration, cloud deployment, and monitoring using AWS, Docker, Jenkins, Kubernetes, Prometheus, and Grafana.


---

Architecture

┌──────────────────┐
                    │     GitHub       │
                    │  Source Code     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │     Jenkins      │
                    │      CI/CD       │
                    └────────┬─────────┘
                             │
                     Docker Build
                             │
                             ▼
                    ┌──────────────────┐
                    │   Docker Hub     │
                    │ Container Images │
                    └────────┬─────────┘
                             │
                             ▼
              ┌─────────────────────────────┐
              │        Kubernetes           │
              │                             │
              │  ┌─────────┐ ┌──────────┐  │
              │  │Frontend │ │   API    │  │
              │  └─────────┘ └────┬─────┘  │
              │                    │        │
              │              ┌─────▼─────┐  │
              │              │   MySQL   │  │
              │              └───────────┘  │
              │                             │
              │        Robot Simulator      │
              └──────────────┬──────────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   Prometheus     │
                    │     Metrics      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │     Grafana      │
                    │    Monitoring    │
                    └──────────────────┘


---

Features

Robot fleet management dashboard

Robot status and battery monitoring

Robot location tracking

Robot activity simulation

REST API built with Flask

MySQL database

Docker containerization

Docker Compose orchestration

Jenkins CI/CD pipeline

Docker Hub image publishing

Kubernetes deployment

Prometheus infrastructure monitoring

Grafana dashboards for CPU, memory, and disk usage



---

Technology Stack

Category	Technology

Cloud	AWS EC2
Frontend	HTML, CSS, JavaScript
Backend	Python, Flask
Database	MySQL 8.0
Containerization	Docker
Container Orchestration	Kubernetes
CI/CD	Jenkins
Image Registry	Docker Hub
Monitoring	Prometheus
Visualization	Grafana
Version Control	Git & GitHub
Operating System	Ubuntu Linux



---

Project Structure

robot-operations-platform/
│
├── index.html
├── Dockerfile
├── docker-compose.yml
│
├── database/
│   └── schema.sql
│
├── robot-api/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── robot-simulator/
│   ├── simulator.py
│   ├── Dockerfile
│   └── requirements.txt
│
└── k8s/
    ├── mysql.yaml
    ├── api.yaml
    ├── simulator.yaml
    └── frontend.yaml


---

Docker

The application is containerized into separate services:

Frontend

Flask API

Robot Simulator

MySQL


Docker Compose is used to run the application stack.

docker compose up -d

Check running containers:

docker compose ps


---

CI/CD with Jenkins

Jenkins automates the application delivery workflow.

Pipeline

GitHub
   ↓
Checkout
   ↓
Build Docker Images
   ↓
Push Images to Docker Hub
   ↓
Deploy to Kubernetes

The Jenkins pipeline automatically builds the application Docker images and pushes them to Docker Hub.


---

Kubernetes

The application is deployed on a Kubernetes cluster running on AWS EC2.

Kubernetes Components

Frontend Deployment

Flask API Deployment

Robot Simulator Deployment

MySQL Deployment

Kubernetes Services

NodePort services for application access


Check cluster status:

kubectl get nodes

Check application pods:

kubectl get pods

Check services:

kubectl get svc


---

Monitoring

Prometheus and Node Exporter are used to collect infrastructure metrics.

Grafana is connected to Prometheus to visualize:

CPU Usage

Memory Usage

Disk Usage


Monitoring provides visibility into the health and resource utilization of the Kubernetes host.


---

DevOps Workflow

Developer
    │
    ▼
 GitHub
    │
    ▼
 Jenkins
    │
    ├── Build
    ├── Test
    └── Docker Build
            │
            ▼
       Docker Hub
            │
            ▼
       Kubernetes
            │
       ┌────┴────┐
       ▼         ▼
 Application   Database
       │
       ▼
 Prometheus
       │
       ▼
 Grafana


---

Project Objectives

This project was developed to gain hands-on experience with:

Linux administration

AWS infrastructure

Git and GitHub

Docker

Docker Compose

Jenkins CI/CD

Kubernetes

Container networking

MySQL

Prometheus

Grafana

DevOps automation
