from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, search

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
   # path('post/post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('results/', views.search, name='search'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='about'),
    path('send/', views.send, name='send'),
    path('delete/<int:com_id>/', views.del_com, name='del_com'),
    path('user/<str:username>', UserPostListView, name='user-posts'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
]
