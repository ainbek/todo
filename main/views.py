from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import ToMeet
def homepage(request):
    return render (request, 'index.html')

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})



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
    return redirect(test)

def unfav_todo(request, id):
    todo =ToDo.objects.get(id=id)
    todo.is_closed = True
    todo.save()
    return redirect(test)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed 
    todo.save()
    return redirect(test)



def tomeet(request):
    item_list = ToMeet.objects.all()
    return render(request, "meeting.html", {"item_list": item_list}) 
def test2(request):
    return HttpResponse ("test2  github page")


def add_tomeet(request):
    form = request.POST
    persone = form["tomeet_text"]
    tomeet = ToMeet(persone=persone)
    tomeet.save()
    return redirect(test2)

def delete_tomeet(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.delete()
    return redirect(test2) 

def fav_tomeet(request, id):
    tomeet =ToMeet.objects.get(id=id)
    tomeet.is_favorite = True
    tomeet.save()
    return redirect(test2)

def unfav_tomeet(request, id):
    tomeet =ToMeet.objects.get(id=id)
    tomeet.is_closed = True
    tomeet.save()
    return redirect(test2)

def close_tomeet(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_closed = not tomeet.is_closed 
    tomeet.save()
    return redirect(test2)