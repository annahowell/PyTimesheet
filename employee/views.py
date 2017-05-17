from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm

from .models import Employee

#def results(request, question_id):
    #question = get_object_or_404(Employee, pk=employee_id)
    #return render(request, 'polls/results.html', {'question': question})




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
    return render(request, 'employee/post_edit.html', {'form': form})