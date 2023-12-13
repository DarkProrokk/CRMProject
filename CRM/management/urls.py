from django.contrib import admin
from django.urls import path, include
from .views import control_page, done_task, create_project, create_task, task_view


urlpatterns = [
    path('', control_page, name='control_page'),
    path('task_done/', done_task, name='task_done'),
    path('create_project/', create_project, name='create_project'),
    path('create_task/', create_task, name='create_task'),
    path('task/<int:pk>/', task_view, name='task')
]
