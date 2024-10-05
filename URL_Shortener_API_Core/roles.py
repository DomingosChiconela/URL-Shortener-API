from rolepermissions.roles import AbstractUserRole




class Normal(AbstractUserRole):
    available_permissions= {
        "Create_url": True,
        "View_url": True,
        "Edit_url": True,
        "Delete_url": True,
        
        
    }
    
    
    
class Admin(AbstractUserRole):
        available_permissions= {
        "Create_url": True,
        "View_url": True,
        "Edit_url": True,
        "Delete_url": True,
        "Create_user": True,
        "View_user": True,
        "Edit_user": True,
        "Delete_user": True,
        
        }
    