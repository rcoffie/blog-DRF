from rest_framework import permissions


class AuthUserPost(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        else:
            return False
