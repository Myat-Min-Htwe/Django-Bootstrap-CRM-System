from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class CustomerModel(models.Model):
    com_name = models.CharField(max_length=100)
    cs_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.TextField()
    industry = models.CharField(max_length=150)
    note = models.TextField(blank=True,null=True)
    modified_date = models.DateField(default=timezone.now,blank=True)
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.com_name


class IndustryModel(models.Model):
    name = models.CharField(max_length=150)


    def __str__(self):
        return self.name
    

class NoteModel(models.Model):
    note = models.TextField()
    assigned_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey('CustomerModel', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.customer.com_name} - Note"
    



class TaskModel(models.Model):
    note = models.OneToOneField(NoteModel, on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Task for {self.note.customer.com_name}"
