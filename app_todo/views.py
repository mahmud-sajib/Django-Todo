from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.

# home/detail view
def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,('Task Added'))
            return redirect('home')
        else:
            messages.warning(request,('Please enter a task'))
            return redirect('home')
    else:
        tasks = List.objects.all()
        return render(request, 'home.html', {'tasks_list':tasks})

# delete view
def delete(request, task_id):
    task = List.objects.get(pk=task_id)
    task.delete()
    messages.success(request,('Task Removed'))
    return redirect('home')

# mark_done view
def mark_done(request, task_id):
    task = List.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return redirect('home')

# edit view
def edit(request, task_id):
    if request.method == 'POST':
        task = List.objects.get(pk=task_id)
        form = ListForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,('Task Updated'))
            return redirect('home')
       
    else:
        task = List.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task':task})
        




