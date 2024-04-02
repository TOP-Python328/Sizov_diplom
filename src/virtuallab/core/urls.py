"""
URL configuration for virtuallab project.

"""
from django.contrib import admin
from django.urls import path

from main import views as mviews
from users import views as uviews
from laboratories import views as lviews

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', mviews.main, name='main'),
    
    path('register', uviews.register_teacher, name='teacher_register'),
    path('login', uviews.login, name='user_login'),
    path('logout', uviews.logout, name='user_logout'),
    
    path('laboratories', lviews.laboratories, name='laboratories'),
    path('add_laboratory', lviews.add_laboratory, name='add_laboratory'),
    path('add_task', lviews.add_task, name='add_task'),
]
