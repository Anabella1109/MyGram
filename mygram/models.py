from django.db import models


class Profile(models.Model):
    photo=models.ImageField(upload_to='dps/')
    bio=models.TextField()

class Image(models.Model):
     name=models.CharField(max_length=100)
     image=models.ImageField(upload_to = 'images/')
     caption=models.TextField()
     likes=models.IntegerField()
     
     profile=models.ForeignKey(Profile)

     def save_image()
class Comment(models.Model):
    comment=models.TextField()
    image=models.ForeignKey(Image,default='timezone.now')




# Create your models here.
