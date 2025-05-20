# Task Tracker API

A simple RESTful API built with FastAPI and SQLAlchemy for managing tasks. The API allows you to create, read, update, and delete tasks, as well as mark them as complete. It uses PostgreSQL as the database and can be run locally or via Docker. It’s designed to be deployed on AWS EC2 or any other cloud provider.

## Table of Contents

* [Features](#features)
* [Tech Stack](#tech-stack)
* [Prerequisites](#prerequisites)
* [Getting Started](#getting-started)

  * [Clone the Repository](#clone-the-repository)
  * [Set Up the Environment](#set-up-the-environment)
  * [Database Configuration](#database-configuration)
  * [Run Locally](#run-locally)
  * [Run with Docker](#run-with-docker)
* [API Documentation](#api-documentation)
* [API Endpoints](#api-endpoints)
* [Project Structure](#project-structure)
* [Contributing](#contributing)
* [License](#license)

## Features

* Create new tasks
* Retrieve all tasks or a single task by ID
* Update task details
* Mark tasks as complete or incomplete
* Delete tasks
* Automatic database migrations
* Interactive API docs with Swagger UI

## Tech Stack

* **Framework:** FastAPI
* **Language:** Python 3.10+
* **ORM:** SQLAlchemy
* **Database:** PostgreSQL
* **Server:** Uvicorn (ASGI)
* **Testing:** Pytest
* **Containerization:** Docker & Docker Compose
* **CI/CD:** GitLab CI

## Prerequisites

* Python 3.10 or higher
* PostgreSQL 13 or higher
* Docker & Docker Compose (optional but recommended)

## Getting Started

### Clone the Repository

```bash
git clone https://gitlab.com/vinayvmathad/task-tracker-api.git
cd task-tracker-api
```

### Set Up the Environment

1. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Copy the example environment file and edit database credentials:

   ```bash
   cp .env.example .env
   ```

### Database Configuration

1. Create a PostgreSQL database for development:

   ```sql
   CREATE DATABASE tasktracker;
   ```
2. Update `.env` with your database URL, e.g.,

   ```dotenv
   DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/tasktracker
   ```
3. Run migrations (if using Alembic):

   ```bash
   alembic upgrade head
   ```

### Run Locally

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open your browser and navigate to [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive API documentation.

### Run with Docker

Ensure Docker and Docker Compose are installed, then:

```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000`.

## API Documentation

Interactive API docs are available at:

* Swagger UI: `/docs`
* ReDoc: `/redoc`

## API Endpoints

| Method | Endpoint           | Description                        |
| ------ | ------------------ | ---------------------------------- |
| POST   | `/tasks/`          | Create a new task                  |
| GET    | `/tasks/`          | Retrieve all tasks                 |
| GET    | `/tasks/{id}`      | Retrieve a task by ID              |
| PUT    | `/tasks/{id}`      | Update a task by ID                |
| PATCH  | `/tasks/{id}/done` | Mark a task as complete/incomplete |
| DELETE | `/tasks/{id}`      | Delete a task by ID                |

## Project Structure

```
task-tracker-api/
├── app/
│   ├── main.py            # FastAPI application instance and router setup
│   ├── models.py          # SQLAlchemy models
│   ├── schemas.py         # Pydantic schemas
│   ├── crud.py            # CRUD helper functions
│   ├── database.py        # Database connection and session handling
│   └── dependencies.py    # Common dependencies (e.g., get_db)
├── alembic/               # Alembic migrations (if used)
├── tests/                 # Pytest test cases
├── .env.example           # Example environment variables file
├── Dockerfile             # Docker image build instructions
├── docker-compose.yml     # Docker Compose setup for app + database
├── requirements.txt       # Python dependencies
├── alembic.ini            # Alembic configuration
└── .gitlab-ci.yml         # GitLab CI/CD pipeline configuration
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/my-feature`)
3. Make your changes
4. Run tests and ensure everything passes
5. Create a merge request

Please follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.
