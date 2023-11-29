from django.db import models

class places(models.Model):
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to='media')
    desc=models.TextField()

    def __str__(self):
        return self.name

class teams(models.Model):
    t_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media')
    desc=models.TextField()

    def __str__(self):
        return self.t_name



