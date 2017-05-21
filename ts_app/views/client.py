from django.contrib.auth.models import User
from django.http import JsonResponse

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.utils import timezone

from ts_app.forms import AddEditClientForm


def IndexView(request):
    if request.method == "POST":
        form = AddEditClientForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.client_created = timezone.now()
            post.client_modified = timezone.now()
            post.client_created_by = request.user.id
            post.client_modified_by = request.user.id
            post.save()
            return redirect('project')
    else:
        form = AddEditClientForm()
    return render(request, 'client_add_edit.html', {'form': form})


# ======================================================
