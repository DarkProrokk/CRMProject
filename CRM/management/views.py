from django.shortcuts import render, redirect, Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from users.models import CustomUser
from .models import Project, Task

def get_context(perm=None, user=None):
    context = {}

    all_projects = Project.objects.all()

    if perm != 'tier_1':
        for project in all_projects:
            context[project] = project.task_set.all().order_by('-is_done')
    else:
        for project in all_projects:
            tasks = project.task_set.filter(user=user).order_by('-is_done')
            if tasks.exists():
                context[project] = tasks

    return context


def control_page(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    if request.user.has_perm('users.tier_3(Admin)') or request.user.has_perm('users.tier_2'):
        data = get_context()
        if request.user.has_perm('users.tier_3(Admin)'):
            perm = 'tier_3(Admin)'
        else:
            perm = 'tier_2'
    else:
        if request.user.is_authenticated:
            data = get_context('tier_1', request.user)
            perm = 'tier_1'
        else:
            perm = 'tier_2'
            data = get_context()
    context = {
        'title': "Панель управления",
        'all_proj': data,
        'perm': perm,
        'users': CustomUser.objects.all()
    }
    return render(request, template_name='management/control_panel.html', context=context)


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


def create_project(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        Project.objects.create(title=title, descriptions=desc, user=request.user)
    return redirect('control_page')


def create_task(request):
    if request.method == 'POST':
        title = request.POST['task_title']
        desc = request.POST['task_desc']
        user = request.POST['task_user']
        date_finish = request.POST['task_date']
        proj = request.POST['task_proj']
        Task.objects.create(title=title, descriptions=desc, user=CustomUser.objects.get(pk=user),
                            date_finish=date_finish, project=Project.objects.get(pk=proj))
    return redirect('control_page')


def task_view(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        return render(request, 'management/task.html', context={'task': task})
    except ObjectDoesNotExist:
        return HttpResponse("Такой задачи не существует", status=404)