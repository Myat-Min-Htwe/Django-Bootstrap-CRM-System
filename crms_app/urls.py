from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="crms"),
    path('add-customer/', views.add_customer, name="add_customer"),
    path('edit-customer/<int:pk>/', views.edit_customer, name="edit_customer"),
    path('delete-customer/<int:pk>/', views.delete_customer, name="delete_customer"),

    path('add-note/<int:pk>/', views.addNote, name="add_note"),
    path('note-list/', views.listNotes, name="note_list"),

    path('add-to-task-list/<int:note_id>/', views.addToTask, name="add_task"),
    path('task-list/', views.listTasks, name="task_list"),
    path('delete-task/<int:note_id>/', views.delete_task, name="delete_task"),

    path('customer_data_chart/', views.opportunity, name="opportunity"),
    path('get_customer_count_data/', views.customer_data, name="customer_data"),
]