from django.db import models


class Profile(models.Model):
    photo=models.ImageField(upload_to='dps/')
    bio=models.TextField()
class Comment(models.Model):
    comment=models.TextField()

class Image(models.Model):
     name=models.CharField(max_length=100)
     image=models.ImageField(upload_to = 'images/')
     caption=models.TextField()
     likes=models.IntegerField()
     comment=models.ForeignKey(Comment)
     profile=models.ForeignKey(Profile)


# Create your models here.
