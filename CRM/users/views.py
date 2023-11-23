from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
# Create your views here.


def authorization(request):
    return render(request, 'users/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'users/signup.html')
        else:
            return HttpResponse('Invalid login')
    return render(request, 'users/signup.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['login']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = CustomUser.objects.create_user(username=username, password=password1)
            user.save()
            return render(request, 'users/signup.html')
        return HttpResponse('Пароли не совпадают')

def logout_view(request):
    logout(request)
    return render(request, 'users/signup.html')