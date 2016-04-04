from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the websites index.")


def test(request):
    context = {
        'content': ['Test-String', 1, 'Wow']
    }
    return render(request, 'test.html', context)
