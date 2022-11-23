from django.contrib import admin

# Register your models here.
from users.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)