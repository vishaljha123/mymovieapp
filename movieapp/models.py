from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime


class Movies(models.Model):
    name = models.CharField(max_length=155)
    location = models.CharField(max_length=155)
    timimg = models.DateTimeField(default=datetime.now,blank=True)


    class Meta:
        ordering  = ["timimg"]

    def __str__(self):
        name = self.name
        location = self.location
        timimg = self.timimg



        return '{}{}{}'.format(self.name, self.location,self.timimg)
