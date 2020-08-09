from django.shortcuts import render

# Create your views here.
from .models import UserProfile
from .forms import UserProfileForm

from django.contrib.auth.models import User


def profile(request):
    profile = UserProfile.objects.get(id=request.user.id)
    return render(request, "profile.html", {"profile": profile})


def update_profile(request):
    profile = UserProfile.objects.get(id=request.user.id)
    form = UserProfileForm(instance=profile)
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            forms.save()
    return render(request, "update_profile.html", {"form": form})

