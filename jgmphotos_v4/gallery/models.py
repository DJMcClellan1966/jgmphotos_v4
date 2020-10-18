from django.db import models

""" create model for images with in-line link to album to show which album image is in"""
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
