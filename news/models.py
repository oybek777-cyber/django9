from django.db import models
from django.utils import timezone
# Create your models here.


class Publishchoice(models.TextChoices):
    cancel='bekor pilish'
    success="to'g'ri"


class StateManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(state=Publishchoice.success)



class Categroy(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class News(models.Model):
    categroy=models.ForeignKey(Categroy,on_delete=models.CASCADE)
    title=models.CharField(max_length=250)
    slug=models.SlugField()
    image=models.ImageField(upload_to='news')
    text=models.TextField()
    create_date=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    state=models.CharField(max_length=40,choices=Publishchoice.choices,default=Publishchoice.cancel)
    publish_time=models.DateTimeField(auto_now=timezone.now())
    
    objects=models.Manager()
    published=StateManager()

    def __str__(self) -> str:
        return self.title
    
class Meta:
    verbose_name='yangilik'
    verbose_name_plural='yangiliklar'
    ordering=('-create_date',)    




class Contact(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField()
    message=models.TextField()


    def __str__(self) -> str:
        return self.email
