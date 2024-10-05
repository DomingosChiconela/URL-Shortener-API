from django.contrib import admin
from .models import Users
from django.contrib.auth import admin as admim_auth_django
from.forms import UserChangeForm ,UserCreationForm




#registrando o meu modelo 
@admin.register(Users)
class UsersAdmin(admim_auth_django.UserAdmin):
    form=UserChangeForm
    add_form=UserCreationForm
    model=Users
    fieldsets=admim_auth_django.UserAdmin.fieldsets + (
        ('Status',{'fields':('status',)}),
    )
    