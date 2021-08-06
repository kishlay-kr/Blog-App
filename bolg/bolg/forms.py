from django import forms 
from .models import Post 

class BlogModelForm(forms.ModelForm):
    img = forms.ImageField()

    class Meta:
        model = Post
        fields = [
            'title',
            'small_desc',
            'full_content',
            
            
            ]
       