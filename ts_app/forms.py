from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from ts_app.models import Event, Project, Activity, Client



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

    project_name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter title here'}
        )
    )

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
