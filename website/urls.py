from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from .views import *

app_name = 'django'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('succes/', Succes.as_view(), name='succes'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', Registration.as_view(), name='signup'),
]