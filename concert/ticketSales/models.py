from django.db import models

# Create your models here.

class concertModel(models.Model):
    name = models.CharField(max_length=100)
    signerName = models.CharField(max_length=100)
    length = models.IntegerField()
    
    def __str__(self):
        return self.signerName

class locationModel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=11)
    capacity = models.IntegerField()
    
    def __str__(self):
        return self.signerName
    
