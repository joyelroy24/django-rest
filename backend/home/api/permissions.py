from rest_framework import permissions

class IsStaffPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    def has_permission(self, request, view):
        user=request.user
        if not user.is_staff:
            print("noooo $$$$$$$$$$4")
            return False
        return super().has_permission(request,view)
    #     print(user.get_all_permissions())
    #     print(user)
    #     if user.is_staff:
    #         if user.has_perm("products.view_product"):
    #             return True
    #         return False
    #     print(user.get_all_permissions())
    #     return False
    
    # def has_object_permission(self, request, view, obj):
    #     return True