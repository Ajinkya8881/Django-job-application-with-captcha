from django import forms
from django_recaptcha.fields import ReCaptchaField

class ApplicationForm(forms.Form):
    # Field for the applicant's first name
    first_name = forms.CharField(
        max_length=80,  # Maximum length of 80 characters
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )

    # Field for the applicant's last name
    last_name = forms.CharField(
        max_length=80,  # Maximum length of 80 characters
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )

    # Field for the applicant's email address
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )

    # Field for Google reCAPTCHA
    captcha = ReCaptchaField(
        widget=forms.ReCaptchaV3,  # Use reCAPTCHA v3 widget
        error_messages={
            'required': 'Please complete the reCAPTCHA.',
            'invalid': 'Invalid reCAPTCHA. Please try again.'
        }
    )
