from django.contrib import admin
from .models import CustomerModel,IndustryModel,NoteModel,TaskModel

# Register your models here.


admin.site.register(CustomerModel)
admin.site.register(IndustryModel)
admin.site.register(NoteModel)
admin.site.register(TaskModel)