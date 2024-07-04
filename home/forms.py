from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'dept', 'salary', 'bonus', 'role', 'phone', 'hire_date']  
        widgets = {
            'hire_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})  
        }
