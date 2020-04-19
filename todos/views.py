from django.shortcuts import render, redirect
from .models import Todo

def create_view(request):
    title = request.POST.get('title')
    if title:
        todo = Todo(title=title)
        todo.save()
        return redirect('list')
    return render(request, "todos/list.html")

def list_view(request):
    todos = Todo.objects.order_by('-date_created')
    context = {
        "list_todo": todos,
    }
    return render(request, "todos/list.html", context)

def update_view(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == "POST":
        new_title = request.POST.get('title')
        print(new_title)
        if new_title:
            todo.title = new_title
            todo.save()
            return redirect("list")
    context = {
        'todo': todo,
    }
    return render(request, "todos/update.html", context)

def delete_view(request, id):
    todo = Todo.objects.get(id=id)
    if todo:
        todo.delete()
        return redirect('list')
    return render(request, "todos/list.html", context)
