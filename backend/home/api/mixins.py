from .permissions import IsStaffPermission
from  rest_framework import permissions

class staffEditorMixin():
    permission_classes=[permissions.IsAdminUser,IsStaffPermission]