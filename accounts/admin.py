from django.contrib import admin

# Register your models here.
from .models import (
    UserProfile,
    Address,
    personal_information,
    educational_information,
)

admin.site.register(UserProfile)
admin.site.register(Address)
admin.site.register(personal_information)
admin.site.register(educational_information)
