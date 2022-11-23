from django.contrib import admin

# Register your models here.
from .models import *
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id","user",'parent_phone']
    list_display_links = ('id',"user")
    save_as = True
    group_fieldsets = True
admin.site.register(Student,StudentAdmin)
admin.site.register(GroupDateTime)
class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ["student",]
    list_display_links = ("student",)
    save_as = True
    group_fieldsets = True
    list_filter = ["student",]
    search_fields = ['student']
admin.site.register(StudentAttendance,StudentAttendanceAdmin)