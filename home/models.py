from django.db import models

# Create your models here.
class AboutUsComment(models.Model):
    name = models.CharField(max_length=250,verbose_name='FIO')
    content = models.TextField(verbose_name='Biz haqimizdagi fikr')
    star1 = models.BooleanField(default=False)
    star2 = models.BooleanField(default=False)
    star3 = models.BooleanField(default=False)
    star4 = models.BooleanField(default=False)
    star5 = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = 'Biz haqimizda fikrlar'
        verbose_name = 'Biz haqimizda fikr'
    def __str__(self):
        return self.name
class AboutInfoTab(models.Model):
    title = models.CharField(max_length=250,verbose_name='Sarlavha')
    content = models.TextField(verbose_name='Qisqacha')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Biz haqimizda tabContentlar'
        verbose_name = 'Biz haqimizda tabContent'
class Gallary(models.Model):
    image = models.ImageField(upload_to='gallary')
    order = models.IntegerField()
    col = models.PositiveSmallIntegerField()
    class Meta:
        verbose_name_plural = 'Galereya '
        verbose_name = 'Galereya '

class Messages(models.Model):
    name = models.CharField(max_length=250, verbose_name='FIO')
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=250,verbose_name='Mavzu')
    content = models.TextField(verbose_name='Xabar')
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Saytdan kelgan xabarlar '
        verbose_name = 'Saytdan kelgan xabar '

    def __str__(self):
        return self.name