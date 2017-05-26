from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from timesheet_app.models import Event, Project, Activity, Client



class AddEditEmployeeForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'is_active'
        )

# ======================================================


class AddEditProjectForm(forms.ModelForm):
    class Meta:

        model = Project
        fields = (
            'project_name',
            'project_description',
            'project_color',
            'client_id',
            'is_active'
        )

        widgets = {
            'project_description': forms.Textarea(attrs={'rows': 8}),
        }


# ======================================================


class AddEditClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
            'client_business_name',
            'client_contact_name',
            'client_phone_number',
            'client_email',
            'client_address1',
            'client_address2',
            'client_postcode',
            'is_active'
        )
