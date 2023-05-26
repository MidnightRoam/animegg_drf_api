from rest_framework import permissions


class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Allow to change data if logged user is staff else read only.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff
