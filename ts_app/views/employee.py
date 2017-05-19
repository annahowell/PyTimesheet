from django.shortcuts import get_object_or_404, render, redirect
from django.http import request
from ts_app.forms.employee import AddEdit


def post_new(request):
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
    return render(request, 'employee/post_edit.html', {'form': form, 'some': some_one})
