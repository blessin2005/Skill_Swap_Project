from rest_framework import permissions


class IsProfileOwner(permissions.BasePermission):
    """
    Allows access only to the owner of the user profile.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user