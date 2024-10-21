from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.author == request.user