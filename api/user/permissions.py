from rest_framework.permissions import BasePermission

class UserViewSetPermissions(BasePermission):
    def has_permission(self, request, view):
        user=request.user
        # if user.is_anonymous:
            # return False
        print(request.user)
        if view.action=='list':
            if user.is_authenticated and user.is_superuser:
                return True
            return False
        if view.action=='retrieve':
            if user.is_authenticated:
                return True
            return False
        if view.action=='partial_update':
            if user.is_authenticated:
                return True
            return False




        return False