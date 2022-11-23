from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('gallery', gallery, name='gallery'),
    path('elements', elements, name='elements'),

]