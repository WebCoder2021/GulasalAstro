from django.shortcuts import render
from .models import *
from news.models import Event
# Create your views here.
def courses (request):
    context = {}
    courses = Course.objects.all().order_by('order')
    context['courses'] = courses
    context['events']= Event.objects.all().order_by('-created')[:6]

    if request.method == 'POST':
        name = request.POST.get('name',False)
        email = request.POST.get('email',False)
        phone = request.POST.get('phone',False)
        course = request.POST.get('course',False)
        if name and email and phone and course:
            new_student = EnrollCourse.objects.create(name=name, email=email, course_id=course, phone=phone)
            new_student.save()
            context['msg_succses'] = True
    return render(request,'courses/courses.html',context)
def courses_detail (request,slug):
    context = {}
    course = Course.objects.filter(slug=slug).first()
    context['courses'] = Course.objects.exclude(slug=slug).all()[:4]
    if request.method == 'POST':
        name = request.POST.get('name',False)
        email = request.POST.get('email',False)
        phone = request.POST.get('phone',False)
        if name and email and phone and course:
            new_student = EnrollCourse.objects.create(name=name, email=email, course=course, phone=phone)
            new_student.save()
            context['msg_succses'] = True
    if request.method == 'POST' and request.POST.get('message',False):
        msg = CourseComment.objects.create(user=request.user, course=course,content=request.POST.get('message',False))
        msg.save()
    context['course'] = course
    context['populars'] = Course.objects.exclude(slug=slug).all()[:4]
    return render(request,'courses/course-details.html',context)