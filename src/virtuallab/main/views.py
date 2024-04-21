from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from laboratories.forms import AddLaboratoryForm
from laboratories.models import Laboratory, Task
from users.forms import AddGroupForm
from users.models import AcademicGroup, Teacher


def main(request):
    return render(
        request,
        'main.html',
    )

@login_required 
def administration(request):
    form1 = AddLaboratoryForm()
    form2 = AddGroupForm()
    
    if request.method == 'POST':
        if request.POST['form'] == 'add_group':
            form = AddGroupForm(request.POST)
            if form.is_valid():
                form.save()
                form2 = AddGroupForm()
        elif request.POST['form'] == 'add_lab':
            form = AddLaboratoryForm(request.POST)
            if form.is_valid():
                form.save()
                form1 = AddLaboratoryForm()       
        
    return render(
        request,
        'administration.html',
        {
            'form1': form1,
            'form2': form2,
            'laboratories': Laboratory.objects.all(),
            'groups': AcademicGroup.objects.order_by('teacher'),
            'tasks': Task.objects.order_by('laboratory'),
            'teachers': Teacher.objects.all(),
        }
    )