from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('SignUp/Student', views.add_student, name='add_student'),
    path('SignUp/Cordinator', views.add_cordinator, name='add_cordinator'),

    # login_Path
    path('login', views.login_page, name='login_page'),
    path('doLogin', views.dologin, name='doLogin'),
    path('doLogout', views.dologout, name='doLogout'),
    
    path('check_email', views.check_email, name='check_email'),
    path('reset_password', views.reset_password, name='reset_password'),

    # profile update
    path('profile', views.profile, name='profile'),
    path('profile/update', views.profile_update, name='profile_update'),
]