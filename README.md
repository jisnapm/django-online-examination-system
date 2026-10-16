# Online Examination System API

A REST API built with **Python, Django, and Django REST Framework** for managing examination questions.

## Features

- Retrieve all questions
- Create new questions
- Retrieve a question by ID
- Update existing questions
- Delete questions
- Validate request data using serializers

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite

## Project Structure

```text
Online_Examination_System/
├── ExamApp/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── Online_Examination_System/
│   ├── settings.py
│   └── urls.py
├── APIDOC.http
├── manage.py
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/jisnapm/django-online-examination-system.git
cd django-online-examination-system
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django djangorestframework
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

Base URL: `http://127.0.0.1:8000`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/questions/` | Retrieve all questions |
| POST | `/questions/` | Create a question |
| GET | `/questions/<id>/` | Retrieve a question by ID |
| PUT | `/questions/<id>/` | Update a question |
| DELETE | `/questions/<id>/` | Delete a question |

## Sample Request

### Create a Question

**POST** `/questions/`

Content-Type: `application/json`

```json
{
  "question": "What is the data type of 10 / 2 in Python?",
  "option_a": "int",
  "option_b": "str",
  "option_c": "float",
  "option_d": "bool",
  "correct_answer": "option_c"
}
```

### Sample Response

```json
{
  "message": "Question created successfully"
}
```

The response format may vary depending on the API implementation.

## Testing

API endpoints can be tested using Postman or the `APIDOC.http` file with a compatible HTTP client, such as the VS Code REST Client extension.

## Learning Outcomes

- Building REST APIs with Django REST Framework
- Working with Django models and serializers
- Implementing CRUD operations
- Validating incoming request data
- Testing APIs using HTTP requests

## Author

**Jisna P M**

GitHub: [@jisnapm](https://github.com/jisnapm)
