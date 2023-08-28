from rest_framework import permissions

class AdminPermission(permissions.BasePermission):
    def has_permission(self,request,view):
        print(request.user)
        if request.user.is_authenticated:
            if request.user.user_type=="Admin":
                return True
        return False
    
class ClientPermission(permissions.BasePermission):
    
    def has_permission(self,request,view):
        print(request.user)
        if request.user.is_authenticated:
            if request.user.user_type=="Client":
                return True
        return False