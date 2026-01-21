# Life Design Backend Service

## Overview

The Life Design Backend Service is a Python-based microservice built using **FastAPI**.  
It serves as the backend engine for a *Life Design Dashboard*, allowing users to log
goal-oriented activities and receive structured insights derived from their behavior.

The project focuses on:
- Clean REST API design
- Clear separation of concerns
- Translating business rules into efficient backend logic
- Scalable architecture suitable for future database integration

The service uses an **in-memory data store** to keep the prototype simple while
demonstrating production-level design patterns.

---

## Tech Stack

- **Python 3.9+**
- **FastAPI** – REST API framework
- **Pydantic** – Data validation and schema enforcement
- **Uvicorn** – ASGI server

---

## Project Structure

```text
life_design_service/
│
├── app/
│   ├── main.py              # Application entry point
│   │
│   ├── api/                 # API route definitions
│   │   ├── activities.py
│   │   ├── dashboard.py
│   │   └── insights.py
│   │
│   ├── models/              # Core data models
│   │   └── activity.py
│   │
│   ├── schemas/             # Request/response schemas
│   │   └── activity_schema.py
│   │
│   ├── services/            # Business & data interpretation logic
│   │   ├── journal_service.py
│   │   └── insight_service.py
│   │
│   └── repository/          # Data access abstraction
│       ├── base.py
│       └── in_memory.py
│
├── requirements.txt
└── README.md

Installation & Running the Server
1. Install dependencies
pip install -r requirements.txt

2. Start the server
uvicorn app.main:app --reload


The API will be available at:
http://127.0.0.1:8000


Interactive API documentation (Swagger UI):
http://127.0.0.1:8000/docs
