from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Post

# Create your views here.

class UserListView(ListView):
    model = Post
    context_object_name = "posts"
    ordering = ['-date_posted']

def PostDetailView(request, pk):
    post_detail = get_object_or_404(Post, pk=pk)
    return render(request, "user_posts/post_detail.html", {'details': post_detail})