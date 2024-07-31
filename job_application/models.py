from django.db import models

class Form(models.Model):
    # Field to store the first name of the applicant
    first_name = models.CharField(max_length=80)  # CharField is used for short text fields with a max length of 80 characters

    # Field to store the last name of the applicant
    last_name = models.CharField(max_length=80)  # CharField is used for short text fields with a max length of 80 characters

    # Field to store the email address of the applicant
    email = models.EmailField()  # EmailField is used to validate and store email addresses

    def __str__(self):
        # Method to return a string representation of the Form instance
        # This method is useful for displaying a human-readable representation of the object
        return f"{self.first_name} {self.last_name}"
