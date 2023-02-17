from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    
    return render(request, 'myapp2/pages/home.html')

def todos( request: HttpRequest ) -> HttpResponse:
    return render(request, 'myapp2/pages/todos.html')

def todo( request: HttpRequest ) -> HttpResponse:
    return render(request, 'myapp2/pages/todo.html')