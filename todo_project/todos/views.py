from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm, SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('todo_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def todo_list(request):
    # Get filter and sort parameters from the request
    status_filter = request.GET.get('status', None)
    priority_filter = request.GET.get('priority', None)
    sort_by = request.GET.get('sort_by', 'created_at')  # default: sort by created_at

    # Start with all todos for the current user
    todos = Todo.objects.filter(user=request.user)

    # Apply status filter if selected
    if status_filter:
        todos = todos.filter(status=status_filter)

    # Apply priority filter if selected
    if priority_filter:
        todos = todos.filter(priority=priority_filter)

    # Sorting by created date or priority
    if sort_by == 'created_at':
        todos = todos.order_by('-created_at')  # newest first
    elif sort_by == 'priority':
        todos = todos.order_by('-priority')  # priority order (can be customized)

    # Pass filtered and sorted todos to context
    context = {
        'todos': todos,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
        'sort_by': sort_by,
    }
    return render(request, 'todo_list.html', context)

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'add_todo.html', {'form': form})

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id, user=request.user)
    todo.delete()
    return redirect('todo_list')

def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'update_todo.html', {'form': form})
