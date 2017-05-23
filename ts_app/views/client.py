from django.contrib.auth.models import User
from django.http import JsonResponse

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.utils import timezone

from ts_app.forms import AddEditClientForm
from ts_app.models import Client


def IndexView(request):
    if request.method == "POST":
        form = AddEditClientForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.client_created_on = timezone.now()
            post.client_modified_on = timezone.now()
            post.client_created_by = request.user.id
            post.client_modified_by = request.user.id
            post.save()
            return redirect('client')
    else:
        form = AddEditClientForm()
        existing_clients = Client.objects.filter(is_active=1)
        return render(request, 'client_add_edit.html', {'form': form, 'existing_clients': existing_clients})


# ======================================================
