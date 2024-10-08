from django.db import models
from  uuid import  uuid4
from Accounts.models  import Users



# Create your models here.



class  Urls(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4, editable=False) 
    original_url = models.URLField(max_length=700)
    short_url = models.URLField(max_length=150)
    click_count = models.IntegerField(default=0)
    user =models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    create_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True) 
    
    
    
    def __str__(self) :
        return self.short_url
    
    
class Visitor(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4, editable=False) 
    name  = models.CharField(max_length=150)
    ip =  models.GenericIPAddressField()
    url =models.ForeignKey(Urls, on_delete=models.DO_NOTHING)
    create_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True) 
    
    def __str__(self) :
        return self.name+ "_"+ self.ip
    

    
    

