from django.db import models

from django.contrib.auth.models import User


class Person(models.Model):
    class Meta:
#        db_table = 'persons'
        abstract = True
        
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )     
    last_name = models.CharField(verbose_name='Фамилия', max_length=30)
    first_name = models.CharField(verbose_name='Имя', max_length=30)
    patr_name = models.CharField(verbose_name='Отчество', max_length=30)
    uid = models.CharField(max_length=10, unique=True)
    organization = models.CharField(max_length=50)

 
class Teacher(Person):
    class Meta:
        db_table = 'teachers'
        
    post = models.CharField(verbose_name='Должность', max_length=100)

    def __repr__(self):
        return f'{self.last_name} {self.first_name}'
        
    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Group(Person):
    class Meta:
        db_table = 'groups'
    
    title = models.CharField(max_length=10) 
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
      
class Schoolboy(models.Model):
    class Meta:
        db_table = 'schoolboys'        

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    


    