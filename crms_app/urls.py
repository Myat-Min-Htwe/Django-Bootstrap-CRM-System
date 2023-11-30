from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="crms"),
    path('add-customer/', views.add_customer, name="add_customer"),
    path('edit-customer/<int:pk>/', views.edit_customer, name="edit_customer"),
    path('delete-customer/<int:pk>/', views.delete_customer, name="delete_customer"),
]