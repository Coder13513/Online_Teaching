from django.db import models

# Create your models here.

class  Chapter(models.Model):
    id=models.AutoField(primary_key=True) 
    number=models.IntegerField(null=False)  
    name=models.CharField(max_length=255)
   

    def __str__(self):
        # return  '{0}/{1}'.format(self.subject_id,self.attendance_date,)
        return '{0},{1}'.format(self.number,self.name )
