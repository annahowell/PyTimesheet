from django.http import HttpResponse


def IndexView(request):
    return HttpResponse("Hello, world. You're at the project index.")