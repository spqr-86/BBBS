from rest_framework import permissions


class IsUsersCity(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.city == request.user.profile.city
