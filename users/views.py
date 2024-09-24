from urllib import request
from django.shortcuts import get_object_or_404, render, redirect

# from django.contrib.auth.forms import
#  UserCreationForm using register form from from.py but inheriting usercreationform
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from users.models import Profile
from .forms import RegisterForm

# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f" successfully created a new account. Login Below❤️ {username}!",
            )
            return redirect("users:login")
        else:
            messages.error(
                request, "Registration failed. Please correct the errors below."
            )
    else:
        form = RegisterForm()

    return render(request, "users/register.html", {"form": form})


@login_required
def profilepage(request):
    user = request.user
    context = {"user": user}
    return render(request, "users/profile.html", context)
