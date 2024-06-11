from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


# Permiso personalizado que permite solo a propietarios editar el objeto.
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user



class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
