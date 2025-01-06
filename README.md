# Docker Setup Guide

This project uses Docker and Docker Compose to run both the frontend and backend services.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)

## Project Structure
```
.
├── frontend/           # React/TypeScript frontend
│   ├── Dockerfile
│   ├── README.md
│   └── tsconfig.app.json
├── backend/            # FastAPI backend
│   ├── app/
│   │   └── main.py
│   ├── Dockerfile
│   ├── README.md
│   └── requirements.txt
├── docker-compose.yml
├── .gitignore
└── README.md
```

## Quick Start

1. Start all services: 
```
docker-compose up -d --build
```

## Available Services

### Frontend
- Port: 5173
- URL: http://localhost:5173
- Technology: React/TypeScript

### Backend
- Port: 8000
- URL: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Technology: FastAPI
