from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('logout/', views.logoutView, name="logout"),
    path('register/', views.register, name='register')
]
