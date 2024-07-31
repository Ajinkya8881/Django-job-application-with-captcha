*Job Application Form*

*Overview*

This project is a simple Django web application for a job application form. It allows users to submit their application details, including their first name, last name, and email address. The form is protected with Google reCAPTCHA to prevent spam. Submitted data is saved in a database, and a confirmation email is sent to the applicant.

*Features*

Form Submission: Users can submit their job application details.
reCAPTCHA Protection: Ensures that submissions are made by humans.
Email Confirmation: Sends a confirmation email to the applicant upon successful submission.
Django Admin: Manage form submissions via Django’s built-in admin interface.

*Technologies Used*

Django: A high-level Python web framework for rapid development.
Google reCAPTCHA: To protect the form from spam and abuse.
Bootstrap: For responsive design and styling.
Docker: For containerization of the application.

*Installation*

*Prerequisites*

Python 3.12 or higher
pip (Python package installer)
Docker (optional, for containerization)

*Setup*

*Clone the Repository:*

git clone https://github.com/Ajinkya8881/Django-job-application-with-captcha.git
cd Django-job-application-with-captcha.git

*Create a Virtual Environment:*

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

*Install Dependencies:*

pip install -r requirements.txt

*Configure Environment Variables:*

Add your Google reCAPTCHA site key and secret key to your environment variables or settings.py file.
Configure your email settings in settings.py.

*Run Migrations:*

python manage.py migrate

*Run the Development Server:*

python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser to access the application.

*Dockerization*

If you prefer to use Docker, follow these steps:

Build the Docker Image:

docker build -t my-django-app .

Run the Docker Container:

docker run -p 8000:8000 my-django-app

Visit http://127.0.0.1:8000/ to access the application running in the Docker container.

*Usage*

Home Page: Users can fill out the job application form.
About Page: Contains information about the company.
Admin Interface: Manage submissions through Django's admin interface. Access it at http://127.0.0.1:8000/admin/.

*Configuration*

*Django Settings*

Email Configuration: Set your email backend and credentials in settings.py:

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-email-password'

reCAPTCHA Keys: Add your Google reCAPTCHA keys in settings.py:

RECAPTCHA_PUBLIC_KEY = 'your-site-key'
RECAPTCHA_PRIVATE_KEY = 'your-secret-key'

Contributing
Feel free to submit pull requests or open issues if you encounter any problems or have suggestions for improvements.
