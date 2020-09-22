from django.db import models
from authentication.models import User

# Create your models here.


class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    User=models.OneToOneField(User,on_delete=models.CASCADE)
   
  
    def __str__(self):
        return F"{self.User}"