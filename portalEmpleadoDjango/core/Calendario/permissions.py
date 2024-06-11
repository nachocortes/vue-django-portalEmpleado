from rest_framework import permissions


# Permiso personalizado que permite solo a propietarios editar el objeto.
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user

#
# class ReadOnlyPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         # Permitir solicitudes GET sin autenticación
#         if request.method == 'GET':
#             return True
#         # Requerir autenticación para otras solicitudes
#         return request.user and request.user.is_authenticated
#
#
# class IsOwner(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             # Permitir métodos de solo lectura para todos
#             return True
#         # Comprobar si el usuario que realiza la solicitud es el propietario del objeto usuario
#         return obj.user == request.user
#
#
# class IsAdmin(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_admin
#
#
# class IsEditor(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_editor
#
#
# class IsUser(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_user
