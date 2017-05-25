from django.contrib.auth.models import User
from django.http import JsonResponse


from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from ts_app.forms import AddEditEmployeeForm


def IndexView(request):
    if request.method == 'POST':
        form = AddEditEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')

    # elif request.is_ajax():
    else:
        form = AddEditEmployeeForm()
        existing_employees = User.objects.filter(is_active=1)
    return render(request, 'employee_add_edit.html', {'form': form, 'existing_employees': existing_employees})


# ======================================================


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'Sorry this username is already taken.'
    return JsonResponse(data)
