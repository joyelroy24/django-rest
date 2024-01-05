from rest_framework import permissions

class IsStaffPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user=request.user
        print(user.get_all_permissions())
        print(user)
        if user.is_staff:
            if user.has_perm("products.view_product"):
                return True
            return False
        print(user.get_all_permissions())
        return False
    
    def has_object_permission(self, request, view, obj):
        return True