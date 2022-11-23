from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.urls import re_path as url
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('courses/', include('courses.urls')),
    path('events/', include('news.urls')),
    path('student/', include('student.urls')),
    path('user/', include('users.urls')),
    path(r'ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    urlpatterns += url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
handler404 = "home.views.bad_request"