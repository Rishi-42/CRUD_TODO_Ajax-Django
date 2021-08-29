from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    return render(request, 'todo/index.html')

def create(request):    
    todo = Todo(task=request.POST['task'])
    todo.save()
    return redirect('/')

def read(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'todo/result.html', context)

def edit(request, id):
    todos = Todo.objects.get(id=id)
    context = {'todo': todos}
    return render(request, 'todo/edit.html', context)

def update(request, id):
    todo = Todo.objects.get(id=id)
    todo.task = request.POST['task']
    todo.save()
    return redirect('/todo/')

def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/todo/')