from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Manager, Task

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('superuser_dashboard')  # Redirect after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')
def superuser_dashboard(request):
    managers = [
        {'name': 'Manager 1', 'status': 'Ready to Work'},
        {'name': 'Manager 2', 'status': 'Assigned'},
    ]
    return render(request, 'superuser_dashboard.html', {'managers': managers})

def manager_dashboard(request):
    tasks = [
        {'id': 101, 'file_name': 'data.xlsx', 'status': 'Pending'},
    ]
    return render(request, 'manager_dashboard.html', {'tasks': tasks})

def assign_task(request):
    if request.method == 'POST':
        # Ensure the manager_id is passed and valid
        manager_id = request.POST.get('manager')  # Get the manager ID from form data
        
        if manager_id:  # Make sure it's not empty
            try:
                manager = Manager.objects.get(id=manager_id)
                print(f"Manager ID: {manager_id}")
  # Retrieve the manager from the DB
                # Your task assignment logic here

            except Manager.DoesNotExist:
                # Handle the case when the manager does not exist
                return render(request, 'error.html', {'message': 'Manager not found'})
        else:
            # Handle the case where no manager ID was provided
            return render(request, 'error.html', {'message': 'No manager selected'})

    return render(request, 'superuser_dashboard.html')

def unassign_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.assigned_to = None
        task.save()

        messages.success(request, f'Task "{task.task_name}" has been unassigned.')
    except Task.DoesNotExist:
        messages.error(request, 'Task not found.')

    return redirect('superuser_dashboard')
def home(request):
    # Redirect to login page or superuser dashboard based on login status
    if request.user.is_authenticated:
        return redirect('superuser_dashboard')  # Redirect to superuser dashboard
    return redirect('login')  # If not authenticated, redirect to login page
