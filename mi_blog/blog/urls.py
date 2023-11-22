from django.urls import path, include
from . import views

# change

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', views.home, name='index'),
    # path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
    path('my-posts/', views.my_posts, name='my-posts'),
]