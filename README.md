# car-management-application

## User Authentication

This feature provides a user authentication system using Django and Django REST Framework (DRF) with JWT tokens for login and token refresh functionality. The system allows users to register, log in, and receive JWT tokens for secure authentication. Users can log in using either their username or email.

## Features

- **User Registration**: Users can sign up by providing a name, username, email, and password.
- **Login**: Users can log in using their username or email with the correct password.
- **JWT Authentication**: Upon successful login, users receive an access token and a refresh token.
- **Token Refresh**: Users can refresh their access token using the refresh token.
- **Custom Authentication**: Custom authentication backend allows login via username or email.
- **Car Management**: Create, update, delete, and search cars owned by the user.

---

## Project Setup

### Prerequisites

- Python 3.x
- Django 3.x or higher
- Django REST Framework
- Django REST Framework Simple JWT for token-based authentication

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/amitkumar0198singh/car-management-application.git
   cd car-management-application
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**:

   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**:

   ```bash
   python manage.py runserver
   ```

### Configuration

In your `settings.py` file, make sure to set the correct configuration for JWT and authentication backend:

```python
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

AUTHENTICATION_BACKENDS = [
    'account.backends.UsernameOrEmailBackend',
    'django.contrib.auth.backends.ModelBackend',  # Keep default backend for admin
]

# Add the 'account' app to INSTALLED_APPS
INSTALLED_APPS = [
    # other apps
    'account',
    'cars',
]
```

---

## API Endpoints

### 1. **User Authentication Endpoints**

#### **User Registration**

- **URL**: `/sign-up/`
- **Method**: `POST`
- **Request Payload**:

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
     "name": "John Doe",
     "username": "johndoe",
     "email": "johndoe@example.com",
     "access_token": "<access_token>",
     "refresh_token": "<refresh_token>"
   }
   ```

#### **User Login**

- **URL**: `/login/`
- **Method**: `POST`
- **Request Payload**:

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
     "name": "John Doe",
     "username": "johndoe",
     "email": "johndoe@example.com",
     "access_token": "<access_token>",
     "refresh_token": "<refresh_token>"
   }
   ```

#### **Token Refresh**

- **URL**: `/refresh-token/`
- **Method**: `POST`
- **Request Payload**:

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

### 2. **Car Management Endpoints**

#### **Get All Cars**

- **URL**: `/cars/get/`
- **Method**: `GET`
- **Authentication Required**: Yes
- **Query Parameters (optional)**:  
  - `search`: Keyword to search for cars by title, description, or tags.
- **Response**:

   ```json
   {
     "status": true,
     "message": "Cars fetched.",
     "cars": [
       {
         "id": 1,
         "title": "My Car",
         "description": "A great car",
         "tags": "sedan, luxury",
         "images": [
           {"image": "url_to_image"}
         ]
       }
     ]
   }
   ```

#### **Get Car Details**

- **URL**: `/cars/get/<id>/`
- **Method**: `GET`
- **Authentication Required**: Yes
- **Response**:

   ```json
   {
     "status": true,
     "message": "Car Fetched",
     "car": {
       "id": 1,
       "title": "My Car",
       "description": "A great car",
       "tags": "sedan, luxury",
       "images": [
         {"image": "url_to_image"}
       ]
     }
   }
   ```

#### **Create Car**

- **URL**: `/cars/create/`
- **Method**: `POST`
- **Authentication Required**: Yes
- **Request Payload**:

   ```json
   {
     "title": "My New Car",
     "description": "Amazing car",
     "tags": "hatchback, economy",
     "images": [<files>]
   }
   ```

- **Response**:

   ```json
   {
     "status": true,
     "message": "Car created.",
     "data": {
       "id": 1,
       "title": "My New Car",
       "description": "Amazing car",
       "tags": "hatchback, economy",
       "images": [
         {"image": "url_to_image"}
       ]
     }
   }
   ```

#### **Update Car**

- **URL**: `/cars/update/<id>/`
- **Method**: `PUT`
- **Authentication Required**: Yes
- **Request Payload**:

   ```json
   {
     "title": "Updated Car",
     "description": "Updated description",
     "tags": "sedan, updated",
     "images": [<new_files>]
   }
   ```

- **Response**:

   ```json
   {
     "status": true,
     "message": "Car updated.",
     "car": {
       "id": 1,
       "title": "Updated Car",
       "description": "Updated description",
       "tags": "sedan, updated",
       "images": [
         {"image": "url_to_new_image"}
       ]
     }
   }
   ```

#### **Delete Car**

- **URL**: `/cars/delete/<id>/`
- **Method**: `DELETE`
- **Authentication Required**: Yes
- **Response**:

   ```json
   {
     "status": true,
     "message": "Car deleted."
   }
   ```

---

## Custom Authentication Backend

The feature uses a custom authentication backend (`UsernameOrEmailBackend`) that allows users to log in using either their username or email.

### Authentication Flow

1. The `LoginView` accepts the user's `username_or_email` and `password`.
2. The `UsernameOrEmailBackend` checks if the provided value matches either the username or email in the database.
3. If the credentials are valid, the user is authenticated, and JWT tokens (access and refresh) are generated and returned.

--- 
