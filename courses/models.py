import re
from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField
from users.models import CustomUser
from master.models import Master
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=250, unique=True,verbose_name='Kurs nomi')
    sub_title = models.CharField(max_length=500,verbose_name='Kurs haqida qisqacha')
    image = models.ImageField(upload_to ='images/courses/',verbose_name='Kursga mos rasm')
    sale = models.CharField(max_length=100,verbose_name='Kurs narxi')
    objective = RichTextField(verbose_name='Kurs haqida umumiy ma\'lumot')
    eligibility = RichTextField(verbose_name='Nega aynan sizning kursingiz')
    slug = models.SlugField(max_length=500,unique=True, verbose_name='Url manzil')
    order = models.IntegerField(null=True, blank=True, default=0,verbose_name='Kurs tartib raqami')
    def course_outlines(self):
        outlines = Course_outline.objects.filter(course__slug=self.slug)
        return outlines
    def comments(self):
        comment = CourseComment.objects.filter(course__slug=self.slug)
        return comment
    def schedule(self):
        comment = Schedule.objects.filter(group__course__slug=self.slug)
        return comment
    def trainers(self):
        return OurGroup.objects.filter(course__slug=self.slug).all()
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bizning kurs"
        verbose_name_plural = "Bizning kurslar"

class Course_outline(models.Model):
    order = models.IntegerField(verbose_name='Tartib raqami')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,verbose_name='Kurs nomi')
    title = models.CharField(max_length=250, verbose_name='Nima o\'tilishi')
    content = models.TextField(max_length=500,verbose_name='Mavzu haqida qisqacha')
    image = models.ImageField(upload_to='images/courses/outline', verbose_name='Mavzuga mos rasm')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Kursda o`tiladiganlar"
        verbose_name_plural = "Kursda o`tiladiganlar"


class CourseComment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    content = models.TextField()
    def __str__(self):
        return self.content

class WeekDay(models.Model):
    name = models.CharField(max_length=100,verbose_name='Hafta kuni')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Hafta kunlari'
        verbose_name = 'Hafta kuni'
class OurGroup(models.Model):
    name = models.CharField(max_length=250,unique=True,verbose_name='Guruh nomi')
    oreder = models.PositiveSmallIntegerField(verbose_name='Tartib raqami')
    started = models.DateTimeField(null=True, blank=True,verbose_name='Dars boshlangan vaqt')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='Kurs')
    master = models.ForeignKey(Master, on_delete=models.CASCADE,verbose_name = 'O`qituvchi')
    class Meta:
        verbose_name_plural ='Guruhlar'
        verbose_name ='Guruh'
    def schedule(self):
        sch = Schedule.objects.filter(group__name=self.name).all()
        return sch
    def __str__(self):
        return self.name
class Schedule(models.Model):
    time = models.TimeField(verbose_name='Dars boshlanishi')
    group = models.ForeignKey(OurGroup, on_delete=models.CASCADE,verbose_name='Guruh')
    order = models.IntegerField(verbose_name='Tartib raqami')
    week = models.ForeignKey(WeekDay, on_delete=models.CASCADE,verbose_name='Hafta kuni')

    def __str__(self):
        return self.group.name
    class Meta:
        verbose_name_plural ='Dars jadvali'
        verbose_name ='Dars jadvali'



class EnrollCourse(models.Model):
    name = models.CharField(max_length=255, verbose_name='FIO')
    phone = models.CharField(max_length=100, verbose_name='Telefon raqami')
    email = models.CharField(max_length=100,blank=True,null=True,verbose_name='Email manzili')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,verbose_name='Qaysi kursga yozilmoqchi')
    date = models.DateTimeField(auto_now_add=True)
    talked = models.BooleanField(default=False,verbose_name='Telefon orqali gaplashildi')
    rejected = models.BooleanField(default=False,verbose_name='Rad etildi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Kursga yozilmoqchi bo\'lganlar'
        verbose_name = 'Kursga yozilmoqchi bo\'lganlar'



