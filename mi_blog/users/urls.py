from django.urls import path
from .views import RegisterView, LoginView
from blog.views import Index as IndexView
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('', IndexView.as_view(), name='index'),
  path('register/', RegisterView.as_view(), name='register'),
  path('login/', LoginView.as_view(), name='login'),
  path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')
]
