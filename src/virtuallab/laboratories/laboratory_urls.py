from django.urls import path

from laboratories import views as lviews


urlpatterns = [
    path('', lviews.laboratories, name='laboratories'),
    path('add', lviews.add_laboratory, name='add_laboratory'),
    path('lab_1', lviews.lab_1, name='lab_1'),
]