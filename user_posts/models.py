from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField("Text")
    date_posted = models.DateTimeField("Date Posted", default=timezone.now)
    sponsored = models.BooleanField("Sponsored", default=False)
    no_of_likes = models.IntegerField(default=0)
    no_of_comments = models.IntegerField(default=0)
    images = models.ImageField(upload_to="user_posts")

    def __str__(self):
        return f"{self.user} post"

# posts of comment section goes here
class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} Comment"


# likes will go here
class Like(models.Model):
    likes = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} Like"
