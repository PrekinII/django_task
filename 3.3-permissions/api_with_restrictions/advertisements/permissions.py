from rest_framework import permissions
#from rest_framework.permissions import BasePermission


class IsOwnerReadOnly(permissions.BasePermission): #L>@ZB2%.9^:d+tM

    # def has_permission(self, request, view):
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #     return bool(request.user.is_staff and request.user)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.creator == request.user or bool(request.user.is_staff)


    # def has_object_permission(self, request, view, obj):
    #     if request.method in ('PATCH', 'PUT', 'DELETE'):
    #         return obj.creator == request.user or bool(request.user.is_staff)
    #     return True
