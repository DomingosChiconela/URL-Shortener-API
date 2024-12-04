
from ninja import Router
from .schema import RegisterUserSchema , ResponseSchema,LoginSchema,MessageSchema
from django.contrib.auth.hashers import make_password
from .models import Users
import re
from django.contrib  import auth
from rest_framework_simplejwt.tokens import AccessToken
from .security  import JWTAuth

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

@router.post("/login",response={200:dict,400:MessageSchema,500:MessageSchema})
def login(request,data:LoginSchema):
    try:
        user= auth.authenticate(username=data.username, password=data.Password)
        if not user:
            return 400,{'Invalid user or Password'}
        #gerando token com base na instancia  do usuario
        access_token = AccessToken.for_user(user)
        
        if not access_token:
            # Erro ao gerar do token
            return 500, {"detail": "Failed to generate access token"}

        
        return 200, {
            "token": str(access_token)
        }
       
    
    except Exception as e:
        print(str(e))
        return 500,{"message":"internal erro"}
        
@router.post("/logout", auth=JWTAuth(), response={200: dict, 400: MessageSchema})
def logout(request):
   
    try:
     
        refresh_token = request.data.get('refresh')

        if not refresh_token:
            return 400, {"message": "Refresh token is required"}

       
        token = RefreshToken(refresh_token)
        token.blacklist()  

        return 200, {"message": "Logout successful"}

    except Exception as e:
        print(str(e))
        return 400, {"message": "Invalid token"} 
    







