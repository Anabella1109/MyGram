from django.db import models

class Image(models.Model):
     name=models.CharField(max_length=100)
     image=models.ImageField(upload_to = 'images/')
     caption=models.TextField()
     likes=models.IntegerField()
     

# Create your models here.
