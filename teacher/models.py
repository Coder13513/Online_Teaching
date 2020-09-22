from django.db import models
from authentication.models import User

# Create your models here.


class Teacher(models.Model):
    id=models.AutoField(primary_key=True)
    User=models.OneToOneField(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=255)
    # class_assigned=models.ForeignKey(Class,on_delete=models.DO_NOTHING) 
    # subject_assigned=models.ForeignKey(Subject,on_delete=models.DO_NOTHING)   
  


    def __str__(self):
        return F"{self.User}"
