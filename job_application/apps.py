from django.apps import AppConfig

class JobApplicationConfig(AppConfig):
    # Specifies the default auto field type to use for primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    
    # The name of the application, which should be the same as the name of the directory
    name = 'job_application'
