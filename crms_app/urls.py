from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="crms"),
    path('add-customer/', views.add_customer, name="add_customer"),
    
]