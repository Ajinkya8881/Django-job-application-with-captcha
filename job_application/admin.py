from django.contrib import admin
from .models import Form

# Define a custom admin interface for the Form model
class FormAdmin(admin.ModelAdmin):
    # Fields that should be searchable in the admin interface
    search_fields = ("first_name", "last_name", "email")
    
    # Fields that should be displayed in the list view of the admin interface
    list_display = ("first_name", "last_name", "email")
    
    # Specify the default ordering of the list view
    ordering = ("first_name",)
    
    # Fields that should be displayed as read-only in the admin interface
    readonly_fields = ("email",)

# Register the Form model with the custom FormAdmin configuration
admin.site.register(Form, FormAdmin)
