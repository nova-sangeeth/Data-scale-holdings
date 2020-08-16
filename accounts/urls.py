from django.conf.urls import url, include

from .views import registration, profile

app_name = "accounts"

urlpatterns = [
    url(r"^profile_reg$", registration, name="registration"),
    url(r"^$", profile, name="profile"),
]
