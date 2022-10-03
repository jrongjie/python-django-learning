from django.shortcuts import render, redirect
from .models import todoList
from .forms import todoListForm

from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    #variable to query data and order it by creation
    todo_items = todoList.objects.order_by('id')

    form = todoListForm()

    # add it to context dictionary then gets passed to the template
    context = {'todo_items' : todo_items, 'form':form}
    return render(request, 'todoList/index.html', context)

@require_POST
def addTodoItem(request):
    form = todoListForm(request.POST)

    if form.is_valid():
        new_todo = todoList(text=request.POST['text'])
        new_todo.save()

    return redirect('index')

def completedTodoItem(request, todo_id):
    todo = todoList.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    todoList.objects.filter(completed__exact=True).delete()
    
    return redirect('index')

def deleteAll(request):
    todoList.objects.all().delete()
    
    return redirect('index')