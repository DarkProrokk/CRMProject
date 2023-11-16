from django.shortcuts import render, redirect
from django.db import models
from users.models import CustomUser
from .models import Project, Task
from django.contrib.auth.decorators import permission_required

def control_page(request):
    if request.user.has_perm('tier_3(Admin)'):
        print('meow')
        perm = 'tier_3(Admin)'
        all_proj = Project.objects.all()
    elif request.user.has_perm('tier_2'):
        all_proj = Project.objects.all()
        perm = 'tier_2'
    else:
        all_proj = []
        for proj in Project.objects.all():
            if proj.task_set.filter(user=request.user):
                all_proj.append(proj)
        perm = 'tier_1'
    context = {
        'title': "Панель управления",
        'all_proj': all_proj,
        'perm': perm
    }
    return render(request, template_name='management/control_panel.html', context=context)

def test(request):
    for i in range(20):
        a = Task()
        time = Task.objects.get(pk=48)
        a.title = 'Test'
        a.date_finish = str(time.date_finish)
        print(time)
        a.descriptions = 'asdasda'
        a.user = CustomUser.objects.get(pk=1)
        a.project = Project.objects.get(pk=5)
        a.save()
    pass

def done_task(request):
    data = request.POST['data']
    data_task = request.POST['data_task']
    current_task = Task.objects.get(pk=int(data_task))
    if data == 'True':
        current_task.is_done = True
    else:
        current_task.is_done = False
    current_task.save()
    return redirect('control_page')