from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
    # Your reCAPTCHA site key
    recaptcha_site_key = ''

    if request.method == 'POST':
        # Handle form submission
        form = ApplicationForm(request.POST)
        if form.is_valid():
            # Form is valid, including reCAPTCHA
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            # Save the form data to the database
            Form.objects.create(first_name=first_name, last_name=last_name, email=email)

            # Prepare and send a confirmation email
            message_body = f"A new job application was submitted. Thank you, {first_name}!"
            email_message = EmailMessage(
                "Form submission confirmation.",
                message_body,
                from_email='',  # Sender email address
                to=[email]  # Recipient email address
            )
            email_message.send()

            # Display a success message to the user
            messages.success(request, 'Form submitted successfully!')
        else:
            # Handle form validation failure (including reCAPTCHA)
            messages.error(request, 'There was an error with your submission. Please try again.')

    else:
        # Initialize an empty form if the request method is GET
        form = ApplicationForm()

    # Render the index page with the form and reCAPTCHA site key
    return render(request, 'index.html', {'form': form, 'recaptcha_site_key': recaptcha_site_key})

def about(request):
    # Render the about page
    return render(request, "about.html")
