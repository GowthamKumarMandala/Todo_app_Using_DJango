from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name="lists"),
    path("update_task/<str:pk>/",views.updateTask,name="update_task"),
    path("delete_task/<str:pk>/",views.deleteTask,name="delete_task"),
]
