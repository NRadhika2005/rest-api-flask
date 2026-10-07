# Student Management REST API

## Task 3 – REST API Development

A beginner-friendly RESTful API built using Flask and SQLite.

### Technologies
- Python
- Flask
- SQLite
- REST API
- JSON
- Postman / Thunder Client
- Git / GitHub

### Features
- Create a student
- Get all students
- Get a student by ID
- Update a student
- Delete a student
- Input validation
- Error handling
- JSON responses
- SQLite database integration

## Project Structure
```text
task-3-rest-api/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── docs/
    └── API_DOCUMENTATION.md
```

`students.db` is created automatically when the application starts.

## Database Model

| Field | Type | Constraint |
|---|---|---|
| id | INTEGER | Primary Key, Auto Increment |
| name | TEXT | Required |
| email | TEXT | Required, Unique |
| course | TEXT | Required |
| age | INTEGER | Required, greater than 0 |

## Installation

### 1. Create a virtual environment
```bash
python -m venv venv
```

### 2. Activate it on Windows
```bash
venv\\Scripts\\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

The API will run at:

`http://127.0.0.1:5000`

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Check API status |
| POST | `/students` | Create student |
| GET | `/students` | Get all students |
| GET | `/students/<id>` | Get one student |
| PUT | `/students/<id>` | Update a student |
| DELETE | `/students/<id>` | Delete a student |

## Example: Create Student

**POST** `/students`

JSON:
```json
{
  "name": "Radhika",
  "email": "radhika@example.com",
  "course": "CSE",
  "age": 21
}
```

Response:
```json
{
  "message": "Student created successfully",
  "student_id": 1
}
```

## Example: Get All Students

**GET** `/students`

Response:
```json
[
  {
    "id": 1,
    "name": "Radhika",
    "email": "radhika@example.com",
    "course": "CSE",
    "age": 21
  }
]
```

## Example: Update Student

**PUT** `/students/1`

JSON:
```json
{
  "name": "Radhika Updated",
  "email": "radhika@example.com",
  "course": "Data Science",
  "age": 22
}
```

Response:
```json
{
  "message": "Student updated successfully"
}
```

## Example: Delete Student

**DELETE** `/students/1`

Response:
```json
{
  "message": "Student deleted successfully"
}
```

## Validation and Error Handling
- Missing required fields → `400 Bad Request`
- Age must be an integer → `400 Bad Request`
- Age must be greater than 0 → `400 Bad Request`
- Duplicate email → `400 Bad Request`
- Student not found → `404 Not Found`
- Unknown route → `404 Not Found`
- Unexpected server error → `500 Internal Server Error`

## Testing

Use Postman or Thunder Client to test all endpoints.

## API Documentation

See `docs/API_DOCUMENTATION.md`.

## Upload to GitHub

```bash
git init
git add .
git commit -m "Task 3 REST API Development"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Do not upload `students.db` or the `venv` folder.
