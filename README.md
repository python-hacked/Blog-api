# Blog-api
Generated token 47f71be8d4bda981ced8b552c7dd0f1de5957120 for user satish
# Django CMS API Project

This project implements a Content Management System (CMS) API using Django and Django Rest Framework.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Python 3.x
- Django 3.x
- Django Rest Framework

## Installation

1. Clone this repository:

    ```bash
    git clone `https://github.com/python-hacked/Blog-api.git`
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser for admin access:

    ```bash
    python manage.py createsuperuser
    ```

## Usage

1. Start the development server:

    ```bash
    python manage.py runserver
    ```

2. Access the admin interface:

    Visit http://127.0.0.1:8000/admin/ in your browser and log in using the superuser credentials.

3. Access the API endpoints:

    Visit http://127.0.0.1:8000/api/ in your browser to explore the API.

## API Endpoints

- **User Registration**: POST `/api/register/`

- **User Login**: POST `/api/login/`

- **User Logout**: POST `/api/logout/`

- **List/Create Posts**: GET/POST `/api/posts/`

- **Retrieve/Update/Delete Post**: GET/PUT/DELETE `/api/posts/<post_id>/`

- **List/Create Likes**: GET/POST `/api/likes/`

- **Retrieve/Update/Delete Like**: GET/PUT/DELETE `/api/likes/<like_id>/`

## Testing

Run the tests to ensure the project's functionality:

```bash
python manage.py test
