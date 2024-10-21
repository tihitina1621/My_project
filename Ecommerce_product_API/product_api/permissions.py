from rest_framework.permissions import BasePermission

class IsAuthenticatedOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.author == request.user