from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    title= models.CharField(null= True, blank=True, max_length=50)
    description=models.TextField(null= True, blank=True)
    complete= models.BooleanField(null= False)


    def __str__(self):
        return self.title

    class Meta:
        ordering=["complete"]
    