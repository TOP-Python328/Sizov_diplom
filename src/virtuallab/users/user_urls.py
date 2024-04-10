from django.urls import path

from users import views as uviews


urlpatterns = [
    path('', uviews.student, name='student'),
    path('tasks', uviews.student_tasks, name='student_tasks'),
]