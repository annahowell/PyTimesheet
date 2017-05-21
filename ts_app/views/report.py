from django.shortcuts import get_object_or_404, render, redirect
from django.http import request
from ts_app.forms import AddEditEmployeeForm


def IndexView(request):
    if request.method == "POST":
        form = AddEditEmployeeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = AddEditEmployeeForm()
        current_user = request.user
        some_one = current_user.id
    return render(request, 'report/post_edit.html', {'form': form, 'some': some_one})
