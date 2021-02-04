from django.db import models

# Create your models here.


class LoginModel(models.Model):
    username=models.CharField(max_length=120)
    password=models.CharField(max_length=120)


    def __str__(self):
        return self.username