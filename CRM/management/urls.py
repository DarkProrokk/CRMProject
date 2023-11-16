from django.contrib import admin
from django.urls import path, include
from .views import control_page, test, done_task


urlpatterns = [
    path('test/', test),
    path('', control_page, name='control_page'),
    path('task_done/', done_task, name='task_done'),
]
