from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    disc=models.TextField()
    image=models.ImageField(upload_to='place')
    
    def __str__(self):
        return self.name
    

class Team(models.Model):
    team=models.CharField(max_length=250)
    desc=models.TextField()
    image=models.ImageField(upload_to='team')
    
    def __str__(self):
        return self.team
    
    
class Destination(models.Model):
    image=models.ImageField(upload_to='destination')
    name=models.CharField(max_length=250)
    desc=models.TextField()
    def __str__(self):
        return self.name
    