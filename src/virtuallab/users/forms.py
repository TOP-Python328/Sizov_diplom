from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import BaseUserCreationForm

from users.models import AcademicGroup


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
        
        
class AddGroupForm(forms.ModelForm):
    class Meta:
        model = AcademicGroup
        fields = ['title','teacher']


class AddSchoolboyForm(BaseUserCreationForm):
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
        label='Учебное заведение',
        max_length=50,
    )
  
#    group_id = forms.ChoiceField(
#        label='класс',
 #       choices= {'': ''} | {
 #           group.id: repr(group)
 #           for group in Group.objects.order_by('title')
 #       },
#    )  
    
    def is_valid(self):
        is_valid = super().is_valid()
        return is_valid
        
    def save(self):
        user = super().save()
        return user