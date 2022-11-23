from django.shortcuts import render

from courses.models import Course,EnrollCourse
from master.models import Master
from news.models import Event,Post
from .models import *
# Create your views here.
def home (request):
    courses = Course.objects.all()
    events = Event.objects.all().order_by('-created')[:6]
    posts = Post.objects.all().order_by('-created')[:4]
    masters = Master.objects.all()
    context = {
        'courses': courses,
        'events':events,
        'posts': posts,
        'masters': masters,

    }
    if request.method == 'POST':
        name = request.POST.get('name',False)
        email = request.POST.get('email',False)
        phone = request.POST.get('phone',False)
        course = request.POST.get('course',False)
        if name and email and phone and course:
            new_student = EnrollCourse.objects.create(name=name, email=email, course_id=course, phone=phone)
            new_student.save()
            context['msg_succses'] = True
    return render(request,'home/index.html',context)
def about (request):
    about_us_comments = AboutUsComment.objects.all()[:8]
    about_info_tab = AboutInfoTab.objects.all()[:4]
    courses = Course.objects.all()
    context = {
        'about_us_comments': about_us_comments,
        'about_info_tab': about_info_tab,
        'courses': courses,
        }
    if request.method == 'POST':
        name = request.POST.get('name',False)
        email = request.POST.get('email',False)
        phone = request.POST.get('phone',False)
        course = request.POST.get('course',False)
        if name and email and phone and course:
            new_student = EnrollCourse.objects.create(name=name, email=email, course_id=course, phone=phone)
            new_student.save()
            context['msg_succses'] = True

    return render(request,'home/about.html',context)

def contact (request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name',False)
        email = request.POST.get('email',False)
        subject = request.POST.get('subject',False)
        content = request.POST.get('message',False)
        print(request.POST)
        if name and email and subject and content:
            msg = Messages.objects.create(name=name,subject=subject, email=email,content=content)
            msg.save()
            context['msg_succses'] = True
    return render(request,'home/contact.html',context)
def gallery (request):
    context = {}
    images = Gallary.objects.all()
    context['images'] = images
    return render(request,'home/gallery.html',context)
def elements(request):
    return render(request,'elements.html')

def bad_request(request,exception=None):
    return render(request,'404.html')