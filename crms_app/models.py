from django.db import models
from django.utils import timezone
# Create your models here.

class CustomerModel(models.Model):
    com_name = models.CharField(max_length=100)
    cs_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.TextField()
    industry = models.CharField(max_length=150)
    modified_date = models.DateField(default=timezone.now,blank=True)
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.com_name

class IndustryModel(models.Model):
    name = models.CharField(max_length=150)


    def __str__(self):
        return self.name