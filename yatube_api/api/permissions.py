from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """ Запрет на изменение записи не автором. """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class GetOnly(permissions.BasePermission):
    """ Разрешается только GET запрос. """

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return False
