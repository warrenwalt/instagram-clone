from django.urls import path
from .views import UserListView, UserDetailView

urlpatterns = [
    path('', UserListView.as_view(), name="home"),
    path('user-detail/<int:pk>', UserDetailView.as_view(), name="user-detail"),
]
