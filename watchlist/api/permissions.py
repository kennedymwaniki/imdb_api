from rest_framework import permissions


class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        admin_permission = bool(request.user and request.user.is_staff)
        return request.method == "GET" or admin_permission
        if request.method in permissions.SAFE_METHODS:
            # check if the request is a safe method
            return True
        else:
            return bool(request.user and request.user.is_staff)

        # return request.method in permissions.SAFE_METHODS or admin_permission
        # or admin_permission = request.user.is_staff and request.user.is_authenticated and request.user


class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # check if the request is a safe method
            return True
        else:
            return obj.user == request.user
