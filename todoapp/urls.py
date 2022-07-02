from django.urls import path
from . import views


urlpatterns = [
    path('see_task/', views.see_task, name='see_task'),
    path('add_Task/', views.add_Task, name='add_Task'),
    path('del_Task/<int:i>/', views.del_Task, name='del_Task'),
]