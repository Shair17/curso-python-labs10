from django.urls import path, include
<<<<<<< HEAD
from .views import Index, DetailArticleView, LikeArticle, Featured, DeleteArticleView
=======
from .views import Index, DetailPostView, LikePost, Featured, DeletePostView
>>>>>>> main

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', Index.as_view(), name='index'),
<<<<<<< HEAD
    path('<int:pk>/', DetailArticleView.as_view(), name='detail_article'),
    path('<int:pk>/like', LikeArticle.as_view(), name='like_article'),
    path('featured/', Featured.as_view(), name='featured'),
    path('<int:pk>/delete', DeleteArticleView.as_view(), name='delete_article')
=======
    path('<int:pk>/', DetailPostView.as_view(), name='detail_post'),
    path('<int:pk>/like', LikePost.as_view(), name='like_post'),
    path('featured/', Featured.as_view(), name='Featured'),
    path('<int:pk>/delete', DeletePostView.as_view(), name='delete_post')
>>>>>>> main
]