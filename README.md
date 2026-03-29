
# CloudLab-Ready
# Project Deliverable 2 Repo

Resume: [resume/TyrellEnglish-Resume (2).pdf](resume/TyrellEnglish-Resume (2).pdf)

## Vision
Diagram of the two components and how they communicate:

```mermaid
flowchart LR
  C[Client] -- REST/HTTP --> A[Component A: API Service]
  A -- REST/HTTP --> B[Component B: Worker Service]
```
## Proposal
Base images (initial plan):
- API service: `python:3.12-slim`
- Worker service: `node:20-alpine`

Reasoning:
- I chose Python for the API because I am most comfortable with it and it has great support for the rest of the services.
- Small, lightweight images
- Fast builds and installs
- Easy to deploy and run on CloudLab



## Build Process

This project uses Docker Compose to build and run two services:

- `api` – a FastAPI-based Python service
- `worker` – a Node.js worker service

The `docker-compose.yml` file builds both containers and starts them together.

### API Container Build

The API Dockerfile uses these instructions:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir fastapi uvicorn
COPY ./src /app/src
EXPOSE 8080



## Networking

This project uses Docker Compose networking. When the services are started together, Docker Compose automatically creates a default bridge network for the project.

### How the containers communicate

The two services in this project are:

- `api`
- `worker`

Because both services are started from the same `docker-compose.yml` file, they are placed on the same internal network. This allows them to communicate with one another by service name.

For example, the worker could connect to the API by using the hostname `api` instead of using an IP address.

### Bridge network

A bridge network allows containers in the same Docker Compose project to communicate while staying isolated from unrelated containers.

In this setup:
- the `api` service is available internally as `api`
- the `worker` service is available internally as `worker`
- port `8080` from the API container is mapped to port `8080` on the host machine

### DNS resolution by container name

Docker Compose includes built-in DNS resolution. This means containers can find each other by service name. Instead of using changing IP addresses, the containers can communicate using names like `api` and `worker`, which makes networking easier and more reliable.
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]



