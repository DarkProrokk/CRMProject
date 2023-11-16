from django.shortcuts import render, redirect

from users.models import CustomUser
from .models import Project, Task


def get_contex(perm=None, user=None):
    context = {}
    all_proj = Project.objects.all()
    if perm != 'tier_1':
        for proj in all_proj:
            context[proj] = proj.task_set.all()
    else:
        for proj in all_proj:
            context[proj] = proj.task_set.filter(user=user)
    return context


def control_page(request):
    if not request.user.has_perm('tier_3(Admin') or not request.user.has_perm('tier_2'):
        if request.user.is_authenticated:
            data = get_contex('tier_1', request.user)
        else:
            data = get_contex()
    else:
        data = get_contex()
    context = {
        'title': "Панель управления",
        'all_proj': data,
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

def meow(request):
    some_text = 'meow'