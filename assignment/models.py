from django.db import models
from teacher.models import Teacher
from student.models import Student

# Create your models here.

class Assignment(models.Model):
    title = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE) 


    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=288)

 
    def __str__(self):
        return self.question


class Choice(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title



class Quiz(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,  blank=True, null=False)
    choices = models.ManyToManyField(Choice)
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='answer', blank=True, null=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='assignment', blank=True, null=True)

    # def __str__(self):
    #     return self.question

    def __str__(self):
        return F"{self.assignment}"
