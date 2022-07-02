from django.shortcuts import render
from .models import TodoListItem
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from django.utils import timezone


def see_task(request):
    all_todo_items = TodoListItem.objects.all().order_by('-id')
    return render(request, 'todoapp/todolist.html',
    {'all_items': all_todo_items})


def add_Task(request):
    x = request.POST['content']
    new_item = TodoListItem(content=x)
    new_item.save()
    return HttpResponseRedirect('/see_task/')



def del_Task(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/see_task/')