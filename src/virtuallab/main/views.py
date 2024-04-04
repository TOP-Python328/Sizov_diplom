from django.shortcuts import render

from users.forms import AddGroupForm


def main(request):
    return render(
        request,
        'main.html',
    )


def administration(request):
    if request.method == 'GET':
        form = AddGroupForm()
    
    elif request.method == 'POST':
        form = AddGroupForm(request.POST)
        if form.is_valid():
            form.save()
            form = AddGroupForm()
        
    return render(
        request,
        'administration.html',
        {
            'form': form,
        }
    )