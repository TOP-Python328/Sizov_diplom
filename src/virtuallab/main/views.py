from django.shortcuts import render

from users.forms import AddGroupForm
from laboratories.forms import AddLaboratoryForm
from laboratories.models import Laboratory

def main(request):
    return render(
        request,
        'main.html',
    )


def administration(request):
    if request.method == 'GET':
        form1 = AddLaboratoryForm()
        form2 = AddGroupForm()
    
    elif request.method == 'POST':
        if request.POST['form'] == 'add_group':
            form = AddGroupForm(request.POST)
            if form.is_valid():
                form.save()
                form2 = AddGroupForm()
        
    return render(
        request,
        'administration.html',
        {
            'form1': form1,
            'form2': form2,
            'laboratories': Laboratory.objects.all(),
        }
    )