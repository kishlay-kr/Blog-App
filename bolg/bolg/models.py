from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 

class Post(models.Model):
    title = models.CharField(max_length = 255)
    small_desc = models.TextField()
    full_content = models.TextField()
    published_on = models.DateTimeField(auto_now_add = True)
    img = models.ImageField(upload_to='images/', blank = True )
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    edited_on = models.DateTimeField(auto_now = True)
    likes = models.ManyToManyField(User, blank = True , related_name = 'likes')

    def get_absolute_url(self):
        return reverse('detail_url', kwargs={'pk':self.id})

    class Meta:
        ordering = ['-published_on']