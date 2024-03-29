from django.db import models

from users.models import Teacher, Schoolboy


class Laboratory(models.Model):
    class Meta:
        db_table = 'laboratories'
    
    title = models.CharField(max_length=20, unique=True)

    def __repr__(self):
        return self.title


class Task(models.Model):
    class Meta:
        db_table = 'tasks'
    
    number = models.CharField(max_length=20)
    description = models.TextField()
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    
    def __repr__(self):
        return f'{self.number}: {description}'


class TaskSolution(models.Model):
    class Meta:
        db_table = 'tasks_solution'
    
    time_start = models.DateTimeField(auto_now_add=True)
    time_end = models.DateTimeField()
    solution = models.CharField(max_length=200)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    users = models.ForeignKey(Schoolboy, on_delete=models.CASCADE)