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
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = AddEditClientForm()
    return render(request, 'client/add_edit.html', {'form': form})


# ======================================================
