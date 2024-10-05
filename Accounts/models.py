from django.contrib.auth.models import  AbstractUser
from django.db import models


# Create your models here.


class Users(AbstractUser):
    Status_choices=(('N','Normal'),
                   ('A','Admin')) 
    
    status = models.CharField(max_length=1,choices=Status_choices)
