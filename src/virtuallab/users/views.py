from django.shortcuts import render, redirect


from django.contrib.auth import (
    authenticate, 
    login as auth_login,
    logout as auth_logout,
)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


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
        form = UserCreationForm()
    
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
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