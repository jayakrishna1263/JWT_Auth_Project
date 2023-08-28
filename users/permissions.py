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
            return request.user.user_type == 'Client' and view.action != 'create'
        return False
        
                

    def has_object_permission(self, request, view, obj):
        return request.user==obj