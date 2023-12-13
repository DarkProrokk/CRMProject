from django.urls import path
from .views import SignupUserViews, logout_view, LoginUserViews, user


urlpatterns = [
    path('', user, name='user'),
    path('signin/', LoginUserViews.as_view(), name='signin'),
    path('signup/', SignupUserViews.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),
]