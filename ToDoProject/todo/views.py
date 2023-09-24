from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo

class TodoList(ListView):
    model = Todo
    context_object_name = "tasks"
    template_name = "todo/todo_list.html"
    
    def get_queryset(self):
        return Todo.objects.all().order_by('-id')

class TodoDetail(DetailView):
    model = Todo
    context_object_name = "task"

class TodoCreate(CreateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("list")
    
class TodoUpdate(UpdateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("list")

class TodoDelete(DeleteView):
    model = Todo
    context_object_name = "task"
    success_url = reverse_lazy("list")