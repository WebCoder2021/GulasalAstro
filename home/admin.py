from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(AboutUsComment)
admin.site.register(AboutInfoTab)
admin.site.register(Gallary)
admin.site.register(Messages)