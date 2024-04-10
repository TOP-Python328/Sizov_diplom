"""
URL configuration for virtuallab project.

"""
from django.contrib import admin
from django.urls import path, include

from main import views as mviews
from users import views as uviews
from laboratories import views as lviews

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', mviews.main, name='main'),    
    path('administration', mviews.administration, name='administration'),
    
    path('register', uviews.register_teacher, name='teacher_register'),
    path('login', uviews.login, name='user_login'),
    path('logout', uviews.logout, name='user_logout'),
    path('teacher', uviews.teacher, name='teacher'),
    path('teacher', include('users.teacher_urls')),
    path('student', include('users.user_urls')),
#    path('teacher/<str:uid>', uviews.teacher, name='teacher'),
    
    path('laboratories', lviews.laboratories, name='laboratories'),
    path('add_laboratory', lviews.add_laboratory, name='add_laboratory'),
    path('add_task', lviews.add_task, name='add_task'),
    path('tasks', lviews.tasks, name='tasks'),

]
