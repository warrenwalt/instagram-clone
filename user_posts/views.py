from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Post

# Create your views here.

class UserListView(ListView):
    model = Post
    context_object_name = "posts"
    ordering = ['-date_posted']