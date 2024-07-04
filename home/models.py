from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    role = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    hire_date = models.DateTimeField(null=True, blank=True)  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
