from django import forms 
from .models import Post 

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'small_desc',
            'full_content',
            'img',
            
            ]
       