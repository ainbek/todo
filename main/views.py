from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import ToMeet
def homepage(request):
    return render (request, 'index.html')

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse ("test2  github page")
def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test) 

def fav_todo(request, id):
    todo =ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return request(test)

def unfav_todo(request, id):
    todo =ToDo.objects.get(id=id)
    todo.is_closed = True
    todo.save()
    return request(test)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed 
    todo.save()
    return request(test)