from django.contrib import admin
from .models import CustomerModel,IndustryModel

# Register your models here.


admin.site.register(CustomerModel)
admin.site.register(IndustryModel)