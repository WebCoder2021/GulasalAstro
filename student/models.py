from re import A
from django.db import models
from courses.models import Course, OurGroup
from users.models import CustomUser
# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,verbose_name="O'quvchi username")
    parent_phone = models.CharField(max_length=100, null=True, blank=True,verbose_name="Ota-ona telefon raqami")
    courses = models.ManyToManyField(OurGroup,verbose_name="O'quvchi qatnashadigan kurslar")
    def student_attendance(self):
        return StudentAttendance.objects.filter(student__user=self.user).first()
    def __str__(self):
        return str(self.user.phone) + ' - ' + str(self.user.first_name) + ' ' + str(self.user.last_name)
    class Meta:
        verbose_name_plural = 'O`quvchilar'
        verbose_name = 'O`quvchi'

class GroupDateTime(models.Model):
    group = models.ForeignKey(OurGroup, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    class Meta:
        verbose_name_plural = 'Sana va vaqt'
        verbose_name = 'Sana va vaqt'
    def __str__(self):
        return str(self.group.name) + ' - ' + str(self.date_time)
class StudentAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    days = models.ManyToManyField(GroupDateTime)
    def __str__(self):
        return str(self.student.user.first_name)+ ' '+str(self.student.user.last_name)

    class Meta:
        verbose_name_plural = 'O`quvchi kelmagan sa na va vaqt'
        verbose_name = 'O`quvchi kelmagan sana va vaqt'
