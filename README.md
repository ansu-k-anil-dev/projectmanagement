# Project Management App

A Django-based project management platform for coordinating academic project work between students and coordinators. The application provides role-based workflows for managing student groups, project topics, submissions, faculty assignments, evaluations, and marks.

## Features

- Student and coordinator registration
- Session-based authentication and logout
- Profile management and password reset flow
- Student group creation and membership management
- Project topic, presentation, record, and project submission workflows
- Faculty assignment and evaluation mark management
- Excel export for evaluation data
- Django admin interface
- Local media file handling for uploaded project documents

## Technology Stack

- Python 3
- Django 5.1.7
- SQLite for local development
- Pillow for image uploads
- OpenPyXL for Excel exports
- HTML, CSS, JavaScript, and Django templates

## Project Structure

```text
ProjectManagementApp/
|-- manage.py
|-- requirements.txt
|-- projectserver/          # Django project configuration
|-- auth_module/            # Registration, login, profiles, and password reset
|-- student_module/         # Student project and submission workflows
|-- cordinator_module/      # Coordinator groups, faculty, and evaluations
|-- templates/              # Shared and role-specific templates
|-- static/                 # Source static assets
|-- media/                  # Local uploaded files (not tracked by Git)
`-- db.sqlite3              # Local database (not tracked by Git)
```

## Getting Started

### Prerequisites

- Python 3.10 or newer
- Git

### Installation

1. Clone the repository and enter the project directory:

	```bash
	git clone https://github.com/ansu-k-anil-dev/projectmanagement.git
	cd projectmanagement
	```

2. Create and activate a virtual environment:

	**Windows PowerShell**

	```powershell
	python -m venv env
	.\env\Scripts\Activate.ps1
	```

	**macOS/Linux**

	```bash
	python3 -m venv env
	source env/bin/activate
	```

3. Install the dependencies:

	```bash
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	```

4. Apply database migrations:

	```bash
	python manage.py migrate
	```

5. Create an administrator account if needed:

	```bash
	python manage.py createsuperuser
	```

6. Start the development server:

	```bash
	python manage.py runserver
	```

	Open http://127.0.0.1:8000/ in a browser.

## Configuration

The application reads `DJANGO_SECRET_KEY` from the environment. For local development, the project has a non-production fallback. Set a unique secret before deploying:

```powershell
$env:DJANGO_SECRET_KEY = "replace-with-a-long-random-secret"
```

Never commit `.env` files, production credentials, uploaded media, or database files. A starter environment file is available at `.env.example`.

## Useful Commands

```bash
# Run Django checks
python manage.py check

# Run tests
python manage.py test

# Collect static files for a deployment environment
python manage.py collectstatic
```

## Application Routes

- `/` - Public landing page
- `/auth/` - Authentication, registration, profiles, and password reset
- `/student/` - Student groups and project submissions
- `/cordinator/` - Coordinator groups, assignments, and evaluations
- `/admin/` - Django administration

## Development Notes

This repository is configured for local development with SQLite and Django's development server. Before deploying to production, configure a production database, set `DEBUG=False`, define `ALLOWED_HOSTS`, configure secure email and storage services, and serve static and media files through a production-ready web server.

## License

No license has been specified for this project yet. Add a license file before distributing or reusing the code publicly.