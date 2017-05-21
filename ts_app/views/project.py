from django.shortcuts import get_object_or_404, render, redirect
from django.http import request
from ts_app.forms import AddEditProjectForm


def IndexView(request):
    form = AddEditProjectForm()
    return render(request, 'project/add_edit.html', {'form': form})

