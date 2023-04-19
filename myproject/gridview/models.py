# Create your models here.
from django.db import models

class Notify(models.Model):
    notification_title = models.CharField(max_length=100)
    notification_text = models.CharField(max_length=500)
    notification_image = models.ImageField(upload_to='images/',blank=True,null=True)
    notication_name = models.CharField(max_length=100,blank=True,null=True,default=" ")
