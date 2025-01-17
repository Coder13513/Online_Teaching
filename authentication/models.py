from django.db import models
from django.contrib.auth.models import AbstractUser
# from utils.models   import  BaseAbstarctModel




class User(AbstractUser):
    user_choice     =(('ADMIN','admin'),('TEACHER','teacher'),('STUDENT','student'))
    email           =   models.EmailField(unique=True,blank=False)
    role            =   models.CharField(verbose_name='user role',choices=user_choice,max_length=20,default='STUDENT')
    school_name     =   models.CharField(max_length=280)

    @property
    def owner(self):
        return self.user
