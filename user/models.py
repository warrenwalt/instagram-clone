from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # posts = models.IntegerField()
    followers = models.IntegerField()
    following = models.IntegerField()
    description = models.TextField()
    prof_pic = models.ImageField(upload_to="prof_pic", default="default.jpg")

    def __str__(self):
        return f"{self.user} Profile"

    def save(self):
        super().save()
        img = Image.open(self.prof_pic.path)

        # check if image is > 300
        if img.height > 300 or img.width > 300:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.prof_pic.path)