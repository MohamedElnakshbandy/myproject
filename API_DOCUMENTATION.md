# FastAPI + PostgreSQL CRUD API Documentation

## Project Overview

This project is a REST API built using FastAPI, PostgreSQL, and SQLAlchemy.

The API allows users to:

- Create users
- Read user information
- Update user information
- Delete users
- Count total users

---

## Base URL

```text
http://127.0.0.1:8000
```

---

## 1. Home Endpoint

### Endpoint

```http
GET /
```

### Description

Checks if the API is running correctly.

### Response

```json
{
  "message": "FastAPI + PostgreSQL is working!"
}
```

---

## 2. Get All Users

### Endpoint

```http
GET /users
```

### Description

Returns a list of all users stored in the database.

### Example Response

```json
[
  {
    "id": 1,
    "name": "Mohamed",
    "email": "mohamed@gmail.com"
  }
]
```

---

## 3. Get User By ID

### Endpoint

```http
GET /users/{user_id}
```

### Description

Returns information about a specific user.

### Example

```http
GET /users/1
```

### Response

```json
{
  "id": 1,
  "name": "Mohamed",
  "email": "mohamed@gmail.com"
}
```

---

## 4. Create User

### Endpoint

```http
POST /users
```

### Description

Creates a new user in the database.

### Request Body

```json
{
  "name": "Ali",
  "email": "ali@gmail.com"
}
```

### Response

```json
{
  "message": "User created successfully",
  "id": 5
}
```

---

## 5. Update User

### Endpoint

```http
PUT /users/{user_id}
```

### Description

Updates an existing user's information.

### Example

```http
PUT /users/1
```

### Request Body

```json
{
  "name": "Mohamed Updated",
  "email": "mohamed_updated@gmail.com"
}
```

### Response

```json
{
  "message": "User updated successfully"
}
```

---

## 6. Delete User

### Endpoint

```http
DELETE /users/{user_id}
```

### Description

Deletes a user from the database.

### Example

```http
DELETE /users/5
```

### Response

```json
{
  "message": "User deleted successfully"
}
```

---

## 7. Count Users

### Endpoint

```http
GET /user-count
```

### Description

Returns the total number of users in the database.

### Response

```json
{
  "total_users": 6
}
```

---

## Technologies Used

- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic
- Uvicorn

---

## API Documentation

FastAPI automatically generates Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

to test all API endpoints.