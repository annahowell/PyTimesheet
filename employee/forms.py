from django import forms

from .models import Employee


class PostForm(forms.ModelForm):

    first_name = forms.CharField(label="First name", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'first_name'}))


    username = forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'name': 'username'
                   }
        )
    )
    password = forms.CharField(label="Password", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'username', 'password', 'disabled')
