from django.urls import path
from .views import UserListView, PostDetailView, register, comments

urlpatterns = [
    path('', UserListView.as_view(), name="home"),
    path('post/<int:pk>/', PostDetailView, name="post"),
    path('register/', register, name='register'),
    path('comment/<int:pk>/', comments, name='comment'),
]
