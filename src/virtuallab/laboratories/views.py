from django.shortcuts import render

from laboratories.models import Laboratory


def add_laboratory(request):  
    if request.method == 'POST':
        Laboratory(title=request.POST['title']).save()
        
    return render(
            request,
            'add_laboratory.html',
        )

def add_task(request):  
    if request.method == 'POST':
        print(request.POST)
        
    return render(
            request,
            'add_task.html',
            {
                'laboratories': Laboratory.objects.all()
            }
        )
        
def laboratories(request):  
    return render(
            request,
            'laboratories.html',
            {
                'laboratories': Laboratory.objects.all()
            }
        )