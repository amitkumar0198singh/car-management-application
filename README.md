# Car Management Application

## Overview

This application provides a user-friendly platform for managing cars, including features for user authentication, car creation, updates, and search functionalities. Authentication uses Django Rest Framework (DRF) with JWT tokens for secure access.

---

## Features

- **User Authentication**:
  - Register, login, and obtain JWT tokens for secure access.
  - Login with username or email.
- **Car Management**:
  - Create, update, delete, and search cars owned by the user.
- **Custom Authentication**:
  - Backend supports login via username or email.

---

## Project Setup

### Prerequisites

- Python 3.x
- Django 3.x or higher
- Django REST Framework
- DRF Simple JWT for token-based authentication

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/amitkumar0198singh/car-management-application.git
   cd car-management-application
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

### **1. User Authentication**

#### **User Registration**
- **Endpoint**: `/sign-up/`
- **Method**: `POST`
- **Payload**:
  ```json
  {
    "name": "John Doe",
    "username": "johndoe",
    "email": "johndoe@example.com",
    "password": "password123",
    "confirm_password": "password123"
  }
  ```
- **Response**:
  ```json
  {
    "status": true,
    "message": "User registered successfully.",
    "access_token": "<access_token>",
    "refresh_token": "<refresh_token>"
  }
  ```

#### **User Login**
- **Endpoint**: `/login/`
- **Method**: `POST`
- **Payload**:
  ```json
  {
    "username_or_email": "johndoe",
    "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
    "status": true,
    "message": "User logged in successfully.",
    "access_token": "<access_token>",
    "refresh_token": "<refresh_token>"
  }
  ```

#### **Token Refresh**
- **Endpoint**: `/refresh-token/`
- **Method**: `POST`
- **Payload**:
  ```json
  {
    "refresh": "<refresh_token>"
  }
  ```
- **Response**:
  ```json
  {
    "access": "<new_access_token>"
  }
  ```

---

### **2. Car Management**

#### **Create a Car**
- **Endpoint**: `/cars/create/`
- **Method**: `POST`
- **Authentication Required**: Yes
- **Payload**:
  ```json
  {
    "title": "My New Car",
    "description": "Amazing car",
    "tags": "luxury, sedan",
    "images": [<file>]
  }
  ```
- **Response**:
  ```json
  {
    "status": true,
    "message": "Car created successfully.",
    "data": {
      "id": 1,
      "title": "My New Car",
      "description": "Amazing car",
      "tags": "luxury, sedan",
      "images": [{"image": "image_url"}]
    }
  }
  ```

#### **Update a Car**
- **Endpoint**: `/cars/update/<id>/`
- **Method**: `PUT`
- **Authentication Required**: Yes
- **Payload**:
  ```json
  {
    "title": "Updated Car",
    "description": "Updated description",
    "tags": "updated, sedan",
    "images": [<file>]
  }
  ```
- **Response**:
  ```json
  {
    "status": true,
    "message": "Car updated successfully.",
    "data": {
      "id": 1,
      "title": "Updated Car",
      "description": "Updated description",
      "tags": "updated, sedan",
      "images": [{"image": "new_image_url"}]
    }
  }
  ```

#### **Delete a Car**
- **Endpoint**: `/cars/delete/<id>/`
- **Method**: `DELETE`
- **Authentication Required**: Yes
- **Response**:
  ```json
  {
    "status": true,
    "message": "Car deleted successfully."
  }
  ```

#### **Fetch All Cars**
- **Endpoint**: `/cars/get/`
- **Method**: `GET`
- **Authentication Required**: Yes
- **Query Parameters (optional)**:
  - `search`: Filter cars by title, description, or tags.
- **Response**:
  ```json
  {
    "status": true,
    "message": "Cars fetched successfully.",
    "data": [
      {
        "id": 1,
        "title": "Car Title",
        "description": "Car description",
        "tags": "tag1, tag2",
        "images": [{"image": "image_url"}]
      }
    ]
  }
  ```

#### **Fetch Car by ID**
- **Endpoint**: `/cars/get/<id>/`
- **Method**: `GET`
- **Authentication Required**: Yes
- **Response**:
  ```json
  {
    "status": true,
    "message": "Car fetched successfully.",
    "data": {
      "id": 1,
      "title": "Car Title",
      "description": "Car description",
      "tags": "tag1, tag2",
      "images": [{"image": "image_url"}]
    }
  }
  ```

---

## Custom Authentication Backend

A custom backend, `UsernameOrEmailBackend`, is implemented to enable login with either username or email, ensuring a flexible and user-friendly authentication process.
