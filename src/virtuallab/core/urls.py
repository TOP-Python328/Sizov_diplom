"""
URL configuration for virtuallab project.

"""
from django.contrib import admin
from django.urls import path

from main import views as mviews
from users import views as uviews

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', mviews.main, name='main'),
    
    path('register', uviews.register_teacher, name='teacher_register'),
    path('login', uviews.login, name='user_login'),
    path('logout', uviews.logout, name='user_logout'),
]
