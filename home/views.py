from django.shortcuts import render, redirect, get_object_or_404

from home.forms import EmployeeForm
from home.models import Employee

from django.contrib import messages

def home(request):
    emp = Employee.objects.all()
    return render(request, 'home.html', {'emp':emp})

def add(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.FILES, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added")
            return redirect('home')
        else:
            messages.error(request, "Sorry, there was an error.")
    else:
        form = EmployeeForm()

    return render(request, 'add.html', {'form': form})

def delete(request, id):
    employee = get_object_or_404(Employee, pk=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('home')  
    return render(request, 'delete.html', {'employee': employee})

def update(request, id):
    detail = get_object_or_404(Employee, pk=id)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=detail)
        if form.is_valid():
            form.save()
            messages.success(request, "Update successful")
            return redirect('home')
    else:
        form = EmployeeForm(instance=detail)
    
    return render(request, 'update.html', {'form': form})