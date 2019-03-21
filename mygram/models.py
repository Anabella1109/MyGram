from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Profile(models.Model):
    photo=models.ImageField(upload_to='dps/')
    bio=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    def save_profile(self):
        self.save()
    def delete_profile(self):
       self.delete()

    def update_bio(self,bio):
         self.bio=bio
         self.save()

class Image(models.Model):
     name=models.CharField(max_length=100)
     image=models.ImageField(upload_to = 'images/')
     caption=HTMLField()
     likes=models.IntegerField()
     pub_date = models.DateTimeField(auto_now_add=True)
     profile=models.ForeignKey(Profile, null=True)
     user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
     
     def save_image(self):
         self.save()

     def delete_image(self):
       self.delete()
       
     def update_caption(self,cap):
         self.caption=cap
         self.save()
    
class Comment(models.Model):
    comment=models.TextField()
    image=models.ForeignKey(Image,default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def save_comment(self):
        self.save()
    def delete_comment(self):
       self.delete()

    def update_comment(self,comment):
         self.comment=comment
         self.save()




# Create your models here.
