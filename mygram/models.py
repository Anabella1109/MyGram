from django.db import models

class Comment(models.Model):
    comment=models.TextField()

class Image(models.Model):
     name=models.CharField(max_length=100)
     image=models.ImageField(upload_to = 'images/')
     caption=models.TextField()
     likes=models.IntegerField()
     comment=models.ForeignKey(Comment)


# Create your models here.
