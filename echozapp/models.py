from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    title = models.CharField(max_length=30)
    content = models.TextField()
    writedate = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)
   # like = models.Field(default=0)


    @property
    def update_counter(self):
        self.count+=1
        self.save()


# Create your models here.
