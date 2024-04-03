from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import BaseUserCreationForm


class AddTeacherForm(BaseUserCreationForm):
    last_name = forms.CharField(
        label='Фамилия',
        max_length=30,
    )
    first_name = forms.CharField(
        label='Имя',
        max_length=30,
    )
    patr_name = forms.CharField(
        label='Отчество',
        max_length=30,
    )
    organization = forms.CharField(
        label='Организация',
        max_length=50,
    )
    post = forms.CharField(
        label='Должность',
        max_length=100,
    )
    
    def is_valid(self):
        is_valid = super().is_valid()
 #       if is_valid:
#            if Teacher.objects.filter(**self.cleaned_data):
#                self.add_error(None, 'такой учитель уже существует')
#                return False
        return is_valid
        
    def save(self):
        user = super().save()
#        print(user)
        return user