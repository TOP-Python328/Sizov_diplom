import random

from django.shortcuts import render, redirect

from django.contrib.auth import (
    authenticate, 
    login as auth_login,
    logout as auth_logout,
)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Group

from laboratories.models import Laboratory, Task, TaskSolution

from users.forms import AddTeacherForm, AddGroupForm, AddSchoolboyForm
from users.models import Teacher, AcademicGroup, Schoolboy


def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
    
    elif request.method == 'POST':
        
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('main', permanent=True)    
    
    return render(
        request,
        'login.html',
        {'form': form}
    )


def logout(request):
    auth_logout(request)
    return redirect('main', permanent=True)


def register_teacher(request):
    if request.method == 'GET':
       # form = UserCreationForm()
        form = AddTeacherForm()
    
    elif request.method == 'POST':
        form = AddTeacherForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                teacher = Teacher(
                        user = user,
                        last_name = request.POST['last_name'],
                        first_name = request.POST['first_name'],
                        patr_name = request.POST['patr_name'],
                        uid = str(random.randint(0, 9999)),
                        organization = request.POST['organization'],
                        post = request.POST['post'],                
                )
                teacher.save()
                group = Group.objects.get(name='Учителя')
                user.groups.add(group)
#                print(teacher)
                return redirect('main', permanent=True)
    
    return render(
        request,
        'register_teacher.html',
        {'form': form}
    )


#def teacher(request, uid: str):
#    teacher = Teacher.objects.get(uid=uid)
#    return render(
#        request, 
#        'teacher.html',
#        {
#            'teacher': teacher,
#            'users': teacher.schoolboy.all(),
#        }
#    ) 
def teacher(request):
    teacher = Teacher.objects.get(user_id=request.user.id)
    user = request.user
    return render(
        request, 
        'teacher.html',
        {
            'teacher': teacher,
            'user': user,
        }
    )    
    
def teacher_tasks(request):
    teacher = Teacher.objects.get(user_id=request.user.id)
    return render(
        request, 
        'teacher_tasks.html',
        {
            'teacher': teacher,
            'tasks': Task.objects.all(),
            'laboratories': Laboratory.objects.all()
        }
    ) 
    
def teacher_users(request):
    teacher = Teacher.objects.get(user_id=request.user.id)
    groups = AcademicGroup.objects.filter(teacher=teacher)
    users = Schoolboy.objects.filter(teacher=teacher)
    return render(
        request, 
        'teacher_users.html',
        {
            'teacher': teacher,
            'groups': groups.order_by('title'),
            'users': users.order_by('last_name'),
        }
    ) 
    
def teacher_setings(request):
    teacher = Teacher.objects.get(user_id=request.user.id)
    groups = AcademicGroup.objects.filter(teacher=teacher)  
    users = Schoolboy.objects.filter(teacher=teacher)
    
    if request.method == 'GET':
        form_group = AddGroupForm()
        form_user = AddSchoolboyForm()
    
    elif request.method == 'POST':
        if request.POST['form'] == 'add_group':
            teacher = Teacher.objects.get(user_id=request.user.id)
            AcademicGroup(title=request.POST['title'],teacher=teacher).save()
            form_group = AddGroupForm()
        elif request.POST['form'] == 'add_user':   
            form = AddSchoolboyForm(request.POST)
            if form.is_valid():
                user = form.save()
                if user:
                    schoolboy = Schoolboy(
                            user = user,
                            last_name = request.POST['last_name'],
                            first_name = request.POST['first_name'],
                            patr_name = request.POST['patr_name'],
                            uid = str(random.randint(0, 9999)),
                            organization = request.POST['organization'],
                            group = AcademicGroup.objects.get(id=int(request.POST['group_id'])),   
                            teacher = teacher,         
                    )
                    schoolboy.save()
                    group = Group.objects.get(name='Ученики')
                    user.groups.add(group) 
                    form_user = AddSchoolboyForm()
                    form_group = AddGroupForm()
                    
    return render(
        request,
        'teacher_setings.html',
        {
            'form_group': form_group,
            'form_user': form_user,
            'groups': groups.order_by('title'),
            'users': users.order_by('last_name'),
        }
    )    
    
def student(request):
    student = Schoolboy.objects.get(user_id=request.user.id)
    user = request.user
    return render(
        request, 
        'student.html',
        {
            'student': student,
            'user': user,
        }
    ) 

def student_tasks(request):
    student = Schoolboy.objects.get(user_id=request.user.id)
    solutions = TaskSolution.objects.filter(user_id=student.user_id)
    return render(
        request, 
        'student_tasks.html',
        {
            'student': student,
            'tasks': Task.objects.all(),
            'solutions': solutions,
            'laboratories': Laboratory.objects.all()
        }
    ) 
    
def assigning_tast(request):
    teacher = Teacher.objects.get(user_id=request.user.id)
    groups = AcademicGroup.objects.filter(teacher=teacher)
    users = Schoolboy.objects.filter(teacher=teacher)
    
    if request.method == 'POST':
         teacher = Teacher.objects.get(user_id=request.user.id)
         user = Schoolboy.objects.get(user_id=request.POST['user_id'])   
         task = Task.objects.get(id=request.POST['task_id'])  

         solution = TaskSolution(
                solution = '',
                status = 'выдано',
                grade = 0,
                scale = 100,
                task = task,
                teacher = teacher,
                user = user,
         )
         solution.save()
        
    return render(
        request, 
        'assigning_task.html',
        {
            'teacher': teacher,
            'laboratories': Laboratory.objects.all(),
            'tasks': Task.objects.all(),
            'groups': groups.order_by('title'),
            'users': users.order_by('last_name'),
        }
    )