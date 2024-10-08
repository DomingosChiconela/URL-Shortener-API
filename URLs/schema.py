from ninja import  ModelSchema,Schema
from . models  import Urls,Visitor




class MessageSchema(Schema):
    message:str
    
    
    
class  UrlSchema(Schema):
    original_url:str
    
class ResponseSchema(Schema):
    message:str
    short_url:str
    
    
class VisitorSchema(ModelSchema):
    class Meta:
        model = Visitor
        fields = ['id', 'name', 'ip', 'create_at']


class ClickInfoSchema(Schema):
    Total_click: int
    visitor_info: list[VisitorSchema]



    
    

    
 
        