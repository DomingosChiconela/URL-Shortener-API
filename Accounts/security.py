# security.py

from ninja.security import HttpBearer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import AccessToken
from .models import Users

class JWTAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
           
            validated_token = AccessToken(token)
            user_id = validated_token['user_id']
            
          
            user = Users.objects.get(id=user_id)
            return user
        except (InvalidToken, TokenError):
            return None
        except Users.DoesNotExist:
            return None
