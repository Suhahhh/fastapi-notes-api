# FastAPI Notes API

## Overview

FastAPI Notes API is a backend application built using FastAPI that allows users to register, authenticate, and manage notes securely. The project demonstrates modern backend development concepts including authentication, database integration, ORM, file uploads, environment variables, and REST API design.

---

## Features

### Authentication

* User Registration
* User Login
* Password Hashing using bcrypt
* JWT Token Generation

### Notes Management

* Create Notes
* View Notes
* Update Notes
* Delete Notes

### Database Integration

* SQLite Database
* SQLAlchemy ORM
* One-to-Many Relationship (User → Notes)

### File Upload

* Upload files through API
* Save files to server storage

### Security

* Password hashing
* Environment variables using .env
* JWT-based authentication

### API Documentation

* Swagger UI documentation
* Automatic request validation using Pydantic

---

## Technologies Used

* Python
* FastAPI
* SQLite
* SQLAlchemy
* Pydantic
* JWT (python-jose)
* Passlib (bcrypt)
* Python-dotenv
* Uvicorn

---

## Project Structure

notes-api/

├── app/

│   ├── auth.py

│   ├── database.py

│   ├── models.py

│   ├── schemas.py

│   └── main.py

│

├── uploads/

├── notes.db

├── .env

└── requirements.txt

---

## API Endpoints

### Authentication

POST /register

POST /login

### Notes

POST /notes

GET /notes

PUT /notes/{note_id}

DELETE /notes/{note_id}

### File Upload

POST /upload

---

## Installation

### Clone Repository

git clone https://github.com/Suhahhh/fastapi-notes-api.git

### Navigate to Project

cd fastapi-notes-api

### Create Virtual Environment

python -m venv venv

### Activate Environment

Windows:

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Run Application

uvicorn app.main:app --reload

---

## Swagger Documentation

After starting the server:

http://127.0.0.1:8000/docs

---

## Concepts Demonstrated

* REST API Development
* Authentication and Authorization
* JWT Tokens
* Password Hashing
* SQLite Database
* SQLAlchemy ORM
* CRUD Operations
* Pydantic Validation
* File Upload Handling
* Environment Variables
* FastAPI Dependency Injection

---

## Author

Fathima Suha

GitHub: https://github.com/Suhahhh
