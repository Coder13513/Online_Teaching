from django.db import models
from subject.models import Subject
from chapter.models import Chapter
from teacher.models import Teacher

# Create your models here.


class Lecture(models.Model):
    lecture_choice     =(('TEXT','text'),('AUDIO','audio'),('VIDEO','video'))

    name=models.CharField(max_length=288)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE) 
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    chapter=models.ForeignKey(Chapter, on_delete=models.CASCADE)
    type_of_lecture = models.CharField(verbose_name='Lecture Type',choices=lecture_choice,max_length=20,default='TEXT')
    text= models.URLField(max_length=255,null=True,blank=True)
    audio= models.URLField(max_length=255,null=True,blank=True)
    video= models.URLField(max_length=255,null=True,blank=True)

    def __str__(self):
          return self.name
