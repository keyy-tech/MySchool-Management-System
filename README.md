# Django School Management System

This is a Django-based school management system that allows you to manage students, classes, subjects, and grades.

## Features

- Manage student information
- Manage class information
- Manage subject information
- Manage grades

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/school-management-system.git
    cd school-management-system
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```sh
    python manage.py migrate
    ```

5. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```sh
    python manage.py runserver
    ```

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin/` to manage students, classes, subjects, and grades.

## Models

### Student

- Personal Information
- Parent Information
- Address Information
- School Information

### Class

- Name
- Academic Year
- Subjects

### Subject

- Name
- Code
- Description

### Grade

- Student
- Subject
- Class Assigned
- Grade Type
- Score
- Term

## Grade Types
- Name

## License

This project is licensed under the MIT License.