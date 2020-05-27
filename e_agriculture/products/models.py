from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class products(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (100 , 100)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    def get_absolute_url(self):
        return reverse('detail',kwargs = {'pk':self.pk })
        
