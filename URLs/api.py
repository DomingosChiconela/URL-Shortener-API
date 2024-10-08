
from ninja import Router
from .schema import *
from .models  import  Urls,Visitor

from django.http  import HttpResponseRedirect
from Accounts.security  import  JWTAuth
from django.shortcuts import get_object_or_404

from .utils  import  generate_short_url






router = Router()




@router.post("/shorten",auth=JWTAuth(),response={201:ResponseSchema, 400:MessageSchema,500:MessageSchema})
def createShortUrl(request,data:UrlSchema):
    "enpoint to create the shortened url passing the original"

    try:
        original_url = data.original_url
        short_url = generate_short_url()

        
        while Urls.objects.filter(short_url=short_url).exists():
            short_url = generate_short_url()

        url_instance = Urls(original_url=original_url, short_url=short_url,user_id=request.auth.id)
        url_instance.save()

        return 201, {"message": "URL created successfully!", "short_url": url_instance.short_url}
    
    except Exception  as e:
        print(str(e))
        return 500, {"message": "Internal server error" }
    
@router.get("/{shortUrl}", response={404: MessageSchema, 500: MessageSchema})
def getOriginalUrl(request, shortUrl:str):
    "Endpoint to be redirected to the original URL passing the shortened URL as a parameter"
    try:
        
        url = get_object_or_404(Urls, short_url=shortUrl)
        
        url.click_count +=1 
        url.save()
        
        
        ip = request.META.get('REMOTE_ADDR')
        visitor_name = request.user.username if request.user.is_authenticated else "Anonymous"
        
        Visitor.objects.create(ip = ip, name =visitor_name,url_id = url.id )
        
        
       
        return HttpResponseRedirect(url.original_url)

    except Exception as e:
        print(str(e))
        return 500, {"message": f"Internal server error  {e}"}
    
    

@router.get("/clickinfo/{shortUrl}",auth=JWTAuth() ,response={200:ClickInfoSchema,403: MessageSchema,404: MessageSchema, 500: MessageSchema})
def getshortUrlInfo(request, shortUrl: str):
    "Endpoint to obtain information about the number of visits the shortened url received and visitor information passing the shortened URL as a parameter"
    try:
        
        url = get_object_or_404(Urls, short_url=shortUrl)
        
        if url and  url.user!= request.auth:
            return 403,{"message": "Access denied. This URL does not belong to you."}
        
        visitors = Visitor.objects.filter(url_id = url.id)
        
        
        return 200, {
            "Total_click": url.click_count,
            "visitor_info": visitors
        }
        

    except Exception as e:
        print(str(e))
        return 500, {"message": f"Internal server error  {e}"}
    
    
    
    
   
    
   
   
    
    
    