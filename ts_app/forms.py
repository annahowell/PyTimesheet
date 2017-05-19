from django import forms

'''
class PostForm(forms.ModelForm):

    first_name = forms.CharField(
        label="First name",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'name': 'first_name'
            }
        )
    )

    last_name = forms.CharField(
        label="Last name",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'name': 'last_name'
            }
        )
    )

    username = forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'name': 'username'
            }
        )
    )

    password = forms.CharField(
        label="Password",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'name': 'password'
            }
        )
    )

    class Meta:
        model = timesheet.Project
        fields = ('first_name', 'last_name', 'username', 'password', 'disabled')'''
