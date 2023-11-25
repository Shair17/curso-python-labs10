from django.urls import path, include
from .views import Index, DetailPostView, LikePost, Featured, DeletePostView

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', Index.as_view(), name='index'),
    path('<int:pk>/', DetailPostView.as_view(), name='detail_Post'),
    path('<int:pk>/like', LikePost.as_view(), name='like_Post'),
    path('featured/', Featured.as_view(), name='featured'),
    path('<int:pk>/delete', DeletePostView.as_view(), name='delete_Post')
]
