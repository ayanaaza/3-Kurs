from django.shortcuts import render
from .models import Task

def kanban_board(request):
    tasks = Task.objects.all()
    return render(request, 'kanban_board.html', {'tasks': tasks})

