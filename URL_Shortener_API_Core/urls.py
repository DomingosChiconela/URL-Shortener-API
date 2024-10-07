
from django.contrib import admin
from django.urls import path,include



from ninja import NinjaAPI

from Accounts.api import  router as accounts_router




api= NinjaAPI()
api.add_router("/accounts/",accounts_router)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    
]


