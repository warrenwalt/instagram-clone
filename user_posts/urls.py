from django.urls import path
from .views import UserListView, PostDetailView

urlpatterns = [
    path('', UserListView.as_view(), name="home"),
    path('post/<int:pk>/', PostDetailView, name="post"),
]
