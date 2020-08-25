from django.conf.urls import url, include

from .views import registration, profile, index

app_name = "accounts"

urlpatterns = [
    url(r"^profile_reg$", registration, name="registration"),
    url(r"^profile$", profile, name="profile"),
    url(r"^$", index, name="index"),
]
