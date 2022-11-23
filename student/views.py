from multiprocessing import context
from django.shortcuts import render,redirect
from courses.models import Course
from .models import Student
# Create your views here.
def student_page(request):
    context= {}
    context['courses'] = Course.objects.all()[:4]
    if request.user.is_authenticated and Student.objects.filter(user=request.user).exists():
        context['student'] = Student.objects.filter(user=request.user).first()
        return render(request,'student/student.html', context)
    return redirect('home')