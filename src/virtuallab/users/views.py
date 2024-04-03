import random


from django.shortcuts import render, redirect


from django.contrib.auth import (
    authenticate, 
    login as auth_login,
    logout as auth_logout,
)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.forms import AddTeacherForm
from users.models import Teacher

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
#                print(teacher)
                return redirect('main', permanent=True)
    
    return render(
        request,
        'register_teacher.html',
        {'form': form}
    )


def register_user(request):
    if request.method == 'GET':
        form = UserCreationForm()
    
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main', permanent=True)
    
    return render(
        request,
        'register_user.html',
        {'form': form}
    )


def teacher(request, uid: str):
#    author = authors_cache[name]
    return render(
        request, 
        'teacher.html',
        {
            'teacher': author,
            'users': teacher.schoolboy.all(),
        }
    )    