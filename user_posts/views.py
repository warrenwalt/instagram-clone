from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Post
from .form import UserRegisterForm, CommentForm
from django.contrib import messages

# Create your views here.


class UserListView(ListView):
    model = Post
    context_object_name = "posts"
    ordering = ['-date_posted']


def PostDetailView(request, pk):
    post_detail = get_object_or_404(Post, pk=pk)
    test = request.get_signed_cookie('name', "warren", max_age=10)
    return render(request, "user_posts/post_detail.html", {'details': post_detail, 'learn': test})


def register(request):
    if request.method == "POST":  # check the type of request is GET
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():  # check if form is valid
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created succesfully for {username}!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user_posts/register.html', {'form': form})


def comments(request):
    if request.method == "POST":
        # get username ot set to the form
        poster = request.user.username
        f = CommentForm(request.POST)
        if f.is_valid():
            f.save()
            messages.info(request, "Comment Added!")
            return redirect('post')
        else:
            err = f.errors
            return HttpResponse(f"<h1>{err}</h1>")
    else:
        f = CommentForm(initial={'comment': 'No SHIT Here Yet!'})
    return render(request, "user_posts/comment.html", {'form': f})
