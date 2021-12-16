from rest_framework.permissions import BasePermission


class PostViewSetPermissions(BasePermission):
    def has_permission(self, request, view):
        _user = request.user
        if view.action == "list":
            if _user.is_authenticated:
                return True
            return False
        if view.action == "create":
            if _user.is_authenticated:
                return True
            return False
        if view.action == "retrieve":
            if _user.is_authenticated:
                return True
            return False
        if view.action == "destroy":
            if _user.is_authenticated:
                return True
            return False
        if view.action == "save_post":
            if _user.is_authenticated:
                return True
            return False
        if view.action == 'unsave_post':
            if _user.is_authenticated:
                return True
            return False

        if view.action == 'saved_post':
            if _user.is_authenticated:
                return True
            return False

        if view.action == 'my_post':
            if _user.is_authenticated:
                return True
            return False


