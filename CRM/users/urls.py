from django.urls import path
from .views import authorization, login_view, signup, logout_view


urlpatterns = [
    path('', authorization, name='auth'),
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),
]