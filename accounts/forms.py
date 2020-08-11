from django import forms
from .models import (
    UserProfile,
    personal_information,
    Address,
    educational_information,
)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"
        exclude = ("user",)


class Personal_details_form(forms.ModelForm):
    class Meta:
        model = personal_information
        fields = "__all__"
        exclude = ("user",)


class User_address_form(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"
        exclude = ("user",)


class educational_info_form(forms.ModelForm):
    class Meta:
        model = educational_information
        fields = "__all__"
        exclude = ("user",)

