from django.urls import path
from .views import RegisterView, LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('register/', RegisterView.as_view(), name='register'),
<<<<<<< HEAD
  path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
=======
  path('login/', LoginView.as_view(), name='login'),
  path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')
>>>>>>> main
]