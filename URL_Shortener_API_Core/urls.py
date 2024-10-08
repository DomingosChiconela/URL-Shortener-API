
from django.contrib import admin
from django.urls import path,include



from ninja import NinjaAPI

from Accounts.api import  router as accounts_router
from URLs.api import  router as urls_router




api = NinjaAPI(
    title="URL Shortener API",  
    description="This API offers functionality for account management and URL shortening. By providing an original URL, the API returns a shortened version, allowing the owner to monitor the number of visits received. Additionally, additional information about each visit, such as the visitor's IP and access time, can be obtained for detailed analysis.",
    version="1.0.0"  
)



api.add_router("/accounts/",accounts_router,tags=["Account"])
api.add_router("/urls/",urls_router,tags=["Url"])


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    
]


