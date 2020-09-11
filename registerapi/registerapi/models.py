from django.db import models

class users(models.Model):
    fullname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    mobile = models.(max_length=30)
    