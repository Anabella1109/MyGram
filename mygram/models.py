from django.db import models


class Profile(models.Model):
    photo=models.ImageField(upload_to='dps/')
    bio=models.TextField()
    
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
     caption=models.TextField()
     likes=models.IntegerField()
     
     profile=models.ForeignKey(Profile)
     
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

    def save_comment(self):
        self.save()
    def delete_comment(self):
       self.delete()

    def update_comment(self,comment):
         self.comment=comment
         self.save()




# Create your models here.
