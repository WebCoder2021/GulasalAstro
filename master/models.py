from django.db import models
from users.models import CustomUser
from ckeditor.fields import RichTextField
# Create your models here.
class Master(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,verbose_name="Mentor usernami")
    content = RichTextField(verbose_name="O'qituvchi haqida qisqacha")
    image = models.ImageField(upload_to='images/master',verbose_name="O'qituvchi rasmi")

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    class Meta:
        verbose_name_plural = 'Mentorlar(O`qituvchilar)'
        verbose_name = 'Mentor(O`qituvchi)'