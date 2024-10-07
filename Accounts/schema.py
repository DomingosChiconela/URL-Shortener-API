from ninja import  ModelSchema,Schema
from . models  import Users




class MessageSchema(Schema):
    message:str

class RegisterUserSchema (Schema):
    username:str
    email: str
    password:str
    confirmPassword: str
    
    
    
class ResponseSchema(ModelSchema):
    
    class Meta:
        model= Users
        fields=[ 'id','username','email']
        
    
class LoginSchema(Schema):
    username: str 
    Password: str 
    
        