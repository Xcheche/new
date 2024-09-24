from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=70, help_text="Enter your full name")
    location = models.CharField(max_length=200)
    image = models.ImageField(
        default="profilepics/profilepic.png", upload_to="profilepics"
    )

    def __str__(self):
        return self.user.username
