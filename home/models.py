from django.db import models




class Employee(models.Model):
    first_name = models.CharField(max_length=150, null=False)
    last_name= models.CharField(max_length=100)
    dept = models.CharField(max_length=160)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role= models.CharField(max_length=100)
    phone= models.IntegerField(default=0)
    hire_date= models.DateTimeField()

    def __str__(self):
        return self.first_name
