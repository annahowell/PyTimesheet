from django import forms

from .models import Employee

class PostForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'username', 'password', 'disabled')