from django.urls import path, include
from .views import Index, DetailPostView, LikePost, Featured, DeletePostView

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', Index.as_view(), name='index'),
    path('<int:pk>/', DetailPostView.as_view(), name='detail_post'),
    path('<int:pk>/like', LikePost.as_view(), name='like_post'),
    path('featured/', Featured.as_view(), name='Featured'),
    path('<int:pk>/delete', DeletePostView.as_view(), name='delete_post')
]