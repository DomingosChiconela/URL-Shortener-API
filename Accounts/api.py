
from ninja import Router
from .schema import RegisterUserSchema , ResponseSchema,LoginSchema,MessageSchema
from django.contrib.auth.hashers import make_password
from .models import Users
import re
from django.contrib  import auth

router = Router()

@router.post("/register",response={201:ResponseSchema, 400:MessageSchema,500:MessageSchema})
def register(request, data: RegisterUserSchema):
    try:
   
        if data.password != data.confirmPassword:
            return 400, {"message": "As senhas devem ser iguais"}
        
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', data.email):
            return 400,  {"message": "The email must be in the correct format"}

        
        if Users.objects.filter(username=data.username).exists():
            return 400, {"message": "This username already exists"}


        if Users.objects.filter(email=data.email).exists():
            return 400, {"message": "This email already exists"}

        password_hash = make_password(data.password)
        
        user = Users.objects.create(username=data.username, password=password_hash, email=data.email, status='N')

        return 201,user
    except Exception as e:
        print(str(e))
        return 500,{"message":"Internal server error"}

@router.post("/login",response={400:MessageSchema,500:MessageSchema})
def login(request,data:LoginSchema):
    try:
        user= auth.authenticate(username=data.username, password=data.Password)
        if not user:
            return 400,{'Invalid user or Password'}
        
        auth.login(request,user)
        return 200,{"message":"Authenticated user"}
    
    except Exception:
        return 500,{"message":"internal erro"}
        
@router.post("/logout")
def logout(request):
    "Endpoint para realizar logout."
    request.session.flush()
    return 200,{"success": True}
    
    








@router.get("/{user_id}",response=ResponseSchema)
def getUser(request,user_id:str):
    
    
    try:
        
        user = Users.objects.get(id= user_id)
        
        if not user:
            return  404,{"message":"user not found"}
        
        return 200, user
        
    except Exception :
        return 500,{"message":"Server internal erro"}


    
    