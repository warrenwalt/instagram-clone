from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    posts = models.IntegerField()
    followers = models.IntegerField()
    following = models.IntegerField()
    description = models.TextField()
    prof_pic = models.ImageField(upload_to="prof_pic", default="default.jpg")

    def __str__(self):
        return f"{self.user} Profile"