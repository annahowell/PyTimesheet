from django.shortcuts import get_object_or_404, render, redirect
from django.http import request

'''
def IndexView(request):
    if request.method == "POST":
        form = AddEdit(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = AddEdit()
        current_user = request.user
        some_one = current_user.id
    return render(request, 'employee/index.html', {'form': form, 'some': some_one})
'''







from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from ts_app.forms import AddEditForm


def IndexView(request):
    if request.method == 'POST':
        form = AddEditForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = AddEditForm()
    return render(request, 'employee/add_edit.html', {'form': form})
