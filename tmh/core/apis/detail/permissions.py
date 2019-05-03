from rest_framework import permissions


class IsEditorOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow editors of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.project.client == request.user or obj.project.designer == request.user