# Online Library Management System (Django)

A modern, full-featured online library management system built with Django. This project allows administrators and students to manage books, users, and issued books with a professional, responsive interface.

## Features

- Student and Admin authentication
- Book management (add, view, delete)
- Student management (register, view, delete, profile edit)
- Issue and return books
- Password reset via email
- Modern UI with Bootstrap 5 and icons
- Animated navigation and footer
- Alerts and feedback for user actions
- Secure password change and reset workflow

## Getting Started

### Prerequisites

- Python 3.8+
- Django 4.2+ (tested up to Django 5.2.1)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bmcouma/online-library-management-python-django.git
   cd online-library-management-python-django
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser (for admin access):
   ```bash
   python manage.py createsuperuser
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

- Access the site at `http://127.0.0.1:8000/`
- Admin login: `/admin_login/`
- Student login: `/student_login/`
- Student registration: `/student_registration/`
- Password reset: `/password_reset/`

## Email Setup (Password Reset)

By default, password reset emails are printed to the console. To use a real email provider, configure these settings in `LibraryManagementSystem/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_email_password'
```

## Folder Structure

```
LibraryManagementSystem/   # Django project settings
library/                  # Main app (models, views, templates)
static/                   # Static files (images, CSS, JS)
templates/                # HTML templates
media/                    # Uploaded files
migrations/               # Django migrations
manage.py                 # Django management script
README.md                 # Project documentation
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

---

Designed and maintained by Bravin M. O
