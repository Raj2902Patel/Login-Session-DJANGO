from django.db import models

# Create your models here.

class registerdata(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email
