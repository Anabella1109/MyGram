from .models import Image
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile', 'pub_date']
    