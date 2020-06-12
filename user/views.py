from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from.models import Profile
from user_posts.models import Post

# Create your views here.
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.filter(user=user).first()
    posts = Post.objects.filter(user=user).first()
    return render(request, "user/profile.html", {"user": user, 'profile': profile, 'posts': posts})