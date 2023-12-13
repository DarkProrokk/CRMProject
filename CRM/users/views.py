from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserCreationForm, UserLoginForm
from .models import CustomUser


def user(request):
    if request.user.is_authenticated:
        done = CustomUser.objects.get(pk=request.user.pk).task_set.filter(is_done=True).count()
        tasks = CustomUser.objects.get(pk=request.user.pk).task_set.all().order_by('-is_done')
        return render(request, 'users/user_page.html', context={'tasks': tasks, 'done': done})
    else:
        return redirect('signin')

def logout_view(request):
    logout(request)
    return redirect('signin')


class SignupUserViews(View):
    form_class = UserCreationForm
    template_name = 'users/signup.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            if password != password2:
                form.add_error('password2', 'Пароли должны совпадать')
            else:
                CustomUser.objects.create_user(username=username, password=password)
        return render(request, self.template_name, {'form': form})


class LoginUserViews(View):
    form_class = UserLoginForm
    template_name = 'users/signin.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('control_page')
        else:
            form.add_error('username', 'Неверное имя пользователя или пароль')
        return render(request, self.template_name, {'form': form})