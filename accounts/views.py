from django.shortcuts import render

# Create your views here.
from .models import UserProfile, educational_information, Address, personal_information
from .forms import (
    UserProfileForm,
    educational_info_form,
    User_address_form,
    Personal_details_form,
)

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


def registration(request):
    user = User.objects.get(username=request.user.username)
    profile = UserProfile(user=user)
    education = educational_information(user=user)
    address = Address(user=user)
    personal = personal_information(user=user)
    form_1 = UserProfileForm(request.POST or None, instance=profile)
    form_2 = educational_info_form(request.POST or None, instance=education)
    form_3 = User_address_form(request.POST or None, instance=address)
    form_4 = Personal_details_form(request.POST or None, instance=personal)
    if request.method == "POST":

        if (
            form_1.is_valid()
            and form_2.is_valid()
            and form_3.is_valid()
            and form_4.is_valid()
            and form_5.is_valid()
        ):
            form_1.save()
            form_2.save()
            form_3.save()
            form_4.save()
            form_5.save()
    return render(
        request,
        "profile.html",
        {"form_1": form_1, "form_2": form_2, "form_3": form_3, "form_4": form_4,},
    )

