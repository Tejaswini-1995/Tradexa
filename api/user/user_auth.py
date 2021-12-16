from django.contrib.auth.backends import ModelBackend
from .models import CustomUserModel as User


class CustomUserAuthBackend(ModelBackend):
    """Return User record if username + (some test) is valid.
    Return None if no match.
    """

    def authenticate(self, request, **kwargs):
        email=None
        if kwargs.get('username'):
            email=kwargs.get('username')
        else:
            email = kwargs.get('email')
        password = kwargs['password']
        try:
            user = User.objects.get(email=email)
            if user.check_password(password) is True:
                return user
        except User.DoesNotExist:
            return None