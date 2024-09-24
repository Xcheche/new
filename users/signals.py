# Importing the 'post_save' signal from Django's 'db.models' module
from django.db.models.signals import post_save

# Importing the built-in User model from Django's 'contrib.auth.models' module
from django.contrib.auth.models import User

# Importing the 'receiver' decorator from Django's 'dispatch' module
from django.dispatch import receiver

# Importing the Profile model from the current application's 'models' module
from .models import Profile


# This decorator registers the 'create_profile' function as a receiver for the 'post_save' signal
# sent by the User model. This means the 'create_profile' function will be called every time a User is saved.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # If a new User instance is created (not just updated), create a corresponding Profile instance.
    if created:
        Profile.objects.create(user=instance)


# This decorator registers the 'save_profile' function as a receiver for the 'post_save' signal
# sent by the User model. This means the 'save_profile' function will be called every time a User is saved.
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # Save the associated Profile instance whenever the User instance is saved.
    instance.profile.save()
