from django.db import models

from django.contrib.auth.models import User


class Person(models.Model):
    class Meta:
        db_table = 'persons'
        
    person = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )     
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    patr_name = models.CharField(max_length=30)

 
class Teacher(models.Model):
    class Meta:
        db_table = 'teachers'
        
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    post = models.CharField(max_length=100)


class Grayd(models.Model):
    class Meta:
        db_table = 'grayds'
    
    title = models.CharField(max_length=10) 
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
      
class Schoolboy(models.Model):
    class Meta:
        db_table = 'schoolboys'
        
#    person = models.OneToOne(Person) 
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    grayd = models.ForeignKey(Grayd, on_delete=models.CASCADE)
    


    