from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user.models import Profile
from .models import Comment


class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CommentForm(forms.ModelForm):
    # user = forms.CharField(max_length=100)

    class Meta:
        model = Comment
        fields = ['comment', 'post', 'user']
        widgets = {'user': forms.HiddenInput(), 'post': forms.HiddenInput()}
