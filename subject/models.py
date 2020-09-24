from django.db import models

# Create your models here.

# from teacher.models import Teacher
from classes.models import Classes

class Subject(models.Model):
    id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=255)
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE,default=1)
    
   

    def __str__(self):
        return self.subject_name 
