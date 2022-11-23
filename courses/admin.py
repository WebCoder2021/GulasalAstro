from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Course_outline)
admin.site.register(CourseComment)
admin.site.register(WeekDay)
admin.site.register(Schedule)
admin.site.register(OurGroup)

class CourseAdmin(admin.ModelAdmin):
    list_display = ["id","name"]
    list_display_links = ('id',"name")
    prepopulated_fields = {'slug':('name',),}
    save_as = True
    group_fieldsets = True
admin.site.register(Course,CourseAdmin)
class EnrollCourseAdmin(admin.ModelAdmin):
    list_display = ["id","name",'phone','email','course','date','talked','rejected']
    list_display_links = ('id',"name")
    save_as = True
    group_fieldsets = True
    list_filter = ["name",'phone','course','talked','rejected']
    search_fields = ['name','phone','email','course']
    list_editable = ['talked','rejected']
admin.site.register(EnrollCourse,EnrollCourseAdmin)