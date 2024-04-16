from django.urls import path

from users import views as uviews


urlpatterns = [
    path('', uviews.teacher, name='teacher'),
    path('tasks', uviews.teacher_tasks, name='teacher_tasks'),
    path('users', uviews.teacher_users, name='teacher_users'),
    path('setings', uviews.teacher_setings, name='teacher_setings'),
    path('assign', uviews.assigning_tast, name='assigning_tast'),
]