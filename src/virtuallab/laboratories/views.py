from django.shortcuts import render

from laboratories.models import Laboratory, Task


def add_laboratory(request):  
    if request.method == 'POST':
        Laboratory(title=request.POST['title'],img=request.POST['img']).save()
        
    return render(
            request,
            'add_laboratory.html',
        )

def add_task(request):  
    if request.method == 'POST':
        #print(request.POST['lab_id'])
        lab_id = int(request.POST['lab_id'])
        #lab = Laboratory.objects.filter(id=lab_id) 
        title = request.POST['number']
        description = request.POST['description']
        solution = request.POST['solution']
        task = Task(
                number = title,
                description = description,
                solution = solution,
                laboratory_id = lab_id,
        )
        task.save()
        #print(task)
        
        
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
        
def tasks(request):  
    return render(
            request,
            'tasks.html',
            {
                'tasks': Task.objects.all(),
                'laboratories': Laboratory.objects.all()
            }
        )