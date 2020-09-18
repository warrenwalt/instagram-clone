from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from user.models import Profile

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField("Text")
    date_posted = models.DateTimeField("Date Posted", default=timezone.now)
    sponsored = models.BooleanField("Sponsored", default=False)
    no_of_likes = models.IntegerField(default=0)
    no_of_comments = models.IntegerField()
    images = models.ImageField(upload_to="user_posts")

    class Meta:
        ordering = ['-no_of_likes', '-date_posted']

    def __str__(self):
        return f"{self.user} post"


# posts of comment section goes here
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} Comment"


# likes will go here
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} Like"
