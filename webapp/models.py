from django.db import models

# Create your models here.
class details(models.Model):
    
    name = models.CharField(max_length = 2000)
    reg_no = models.CharField(max_length = 2000)
    course = models.CharField(max_length = 2000)
    batch = models.CharField(max_length = 100) 
    image = models.ImageField(upload_to = 'images')
    
    def _str_(self):
        return self.name    

class leave(models.Model):
    
    name = models.CharField(max_length = 2000)
    email = models.CharField(max_length = 2000)
    date = models.DateField()
    Reason = models.TextField(blank=True)

    def _str_(self):
        return self.name

class disp(models.Model):
    dates=models.DateField()
    files = models.FileField(upload_to = 'images')

    def _str_(self):
        return self.dates