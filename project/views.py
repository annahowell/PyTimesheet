from django.shortcuts import get_object_or_404, render, redirect
from django.http import request
from .forms import PostForm

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = PostForm()
        current_user = request.user
        some_one = current_user.id
    return render(request, 'employee/post_edit.html', {'form': form, 'some': some_one})


def IndexView(request):
    return HttpResponse("Hello, world. You're at the project index.")