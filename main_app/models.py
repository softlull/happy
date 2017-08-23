from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Happy(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    power = models.CharField(max_length=50)
    image = models.ImageField(upload_to='happy_images',
                              default='media/default.png')
    likes = models.IntegerField(default=0)
#     class Meta:
#         ordering = ['likes']
    
    def __str__(self):
        return self.name + " " + self.colour + " " + self.power