from django.urls import path
from .views import *
urlpatterns = [
    path('', courses, name='courses'),
    path('<slug:slug>/detail', courses_detail, name='course_detail'),
]