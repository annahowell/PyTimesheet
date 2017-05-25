from django.shortcuts import get_object_or_404, render, redirect
from django.http import request
from ts_app.forms import AddEditProjectForm
from ts_app.models import Client, Project



def IndexView(request):
    form = AddEditProjectForm()
    existing_projects = Project.objects.filter(is_active=1)
    existing_clients = Client.objects.filter(is_active=1)
    return render(request, 'project_add_edit.html', {'form': form, 'existing_projects': existing_projects, 'existing_clients': existing_clients})

