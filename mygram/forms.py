from .models import Image
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile', 'pub_date','likes']

class NewCommentForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

    