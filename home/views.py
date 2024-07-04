from django.shortcuts import render, redirect, get_object_or_404

from home.forms import EmployeeForm
from home.models import Employee

from django.contrib import messages

from django.db.models import Q

def home(request):
    emp = Employee.objects.all()
    if request.method == 'GET':
        st = request.GET.get('searchbox')
        if st is not None:
            emp = Employee.objects.filter(
                Q(first_name__icontains=st) | Q(last_name__icontains=st)
            )
    return render(request, 'home.html', {'emp': emp})
def add(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added")
            return redirect('home')
        else:
            print(form.errors) 
            messages.error(request, "Sorry, there was an error.")
    
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