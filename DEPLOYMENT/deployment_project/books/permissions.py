from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminRole(BasePermission):
    """Allow access only to users with role='admin'."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class IsEditorOrAdmin(BasePermission):
    """Editors and admins can write; viewers can only read."""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        return request.user.is_authenticated and request.user.is_editor


class IsOwnerOrAdmin(BasePermission):
    """Object-level: owner or admin may modify, others may read."""

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user or request.user.is_admin
