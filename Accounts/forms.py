from  django.contrib.auth import  forms

from Accounts.models import  Users


#sobre escrevendo o form  da area administiva(formulario para editar o usuario) do django para se basei  no meu modelo 
class UserChangeForm(forms.UserChangeForm):
    
    class Meta(forms.UserChangeForm.Meta):
        model= Users
        
        
        
#sobre escrevendo o form  da area administiva(formulario para criar o usuario) do django para se basei  no meu modelo      
class UserCreationForm(forms.UserCreationForm):
    
    class Meta(forms.UserCreationForm.Meta):
        model= Users
        
        
        
        







