# API Documentation – Student Management REST API

## Base URL
`http://127.0.0.1:5000`

## 1. Check API Status

### GET `/`

Response:
```json
{
  "message": "Welcome to Student Management REST API",
  "status": "API is running"
}
```

Status: `200 OK`

## 2. Create Student

### POST `/students`

Request Header: `Content-Type: application/json`

Request Body:
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

Status: `201 Created`

## 3. Get All Students

### GET `/students`

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

Status: `200 OK`

## 4. Get Student by ID

### GET `/students/1`

Response:
```json
{
  "id": 1,
  "name": "Radhika",
  "email": "radhika@example.com",
  "course": "CSE",
  "age": 21
}
```

Status: `200 OK`

If the ID does not exist:
```json
{
  "error": "Student not found"
}
```

Status: `404 Not Found`

## 5. Update Student

### PUT `/students/1`

Request Body:
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

Status: `200 OK`

## 6. Delete Student

### DELETE `/students/1`

Response:
```json
{
  "message": "Student deleted successfully"
}
```

Status: `200 OK`

## Database Model

Table: `students`

| Field | Type | Constraint |
|---|---|---|
| id | INTEGER | Primary Key, Auto Increment |
| name | TEXT | NOT NULL |
| email | TEXT | NOT NULL, UNIQUE |
| course | TEXT | NOT NULL |
| age | INTEGER | NOT NULL |

## Validation Rules

1. `name` is required.
2. `email` is required and must be unique.
3. `course` is required.
4. `age` is required and must be an integer.
5. `age` must be greater than 0.

## HTTP Status Codes

| Code | Meaning |
|---|---|
| 200 | Success |
| 201 | Resource Created |
| 400 | Bad Request / Validation Error |
| 404 | Resource or Route Not Found |
| 500 | Internal Server Error |

## CRUD Summary

| Operation | Method | Endpoint |
|---|---|---|
| Create | POST | `/students` |
| Read All | GET | `/students` |
| Read One | GET | `/students/<id>` |
| Update | PUT | `/students/<id>` |
| Delete | DELETE | `/students/<id>` |
