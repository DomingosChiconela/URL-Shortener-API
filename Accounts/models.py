from django.contrib.auth.models import  AbstractUser
from django.db import models

from  uuid import  uuid4


# Create your models here.


class Users(AbstractUser):
    id = models.UUIDField(primary_key=True,default=uuid4, editable=False)
    Status_choices=(('N','Normal'),
                   ('A','Admin')) 
    
    status = models.CharField(max_length=1,choices=Status_choices)
