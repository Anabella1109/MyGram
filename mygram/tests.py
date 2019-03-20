from django.test import TestCase
from .models import Image,Profile,Comment

class ImageTestClass(TestCase):
       def setUp(self):
          
          self.profile=Profile(id=1234,photo='Rwanda',bio='Kigali')
          self.image=Image(image='@heroo',name='koko',caption="koko koko koko okruuuuuu",likes=2,profile=self.profile)
          self.comment=Comment(id=2134,comment='food',image=self.image)

       def tearDown(self):
           Profile.objects.all().delete()
           Image.objects.all().delete()
           Comment.objects.all().delete()

       def test_save_image(self):
         self.image.save_image()
         images = Image.objects.all()
         self.assertTrue(len(images) > 0)   

       def test_delete_image(self):
           self.image.save_image()
           self.image.delete_image()
           images = Image.objects.all()
           self.assertTrue(len(images) == 0)  
           
# Create your tests here.
