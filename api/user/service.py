from django.http.request import QueryDict
from google.auth.transport import Request
from rest_framework.exceptions import NotFound
from .serializers import UserSerializer
from api.utils import APIError
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .models import CustomUserModel


def getUserByEmail(email):
    user = get_user_model().objects.filter(email=email)
    print(user)
    if len(user) == 0:
        return False
    return user[0]


def getUserById(id):
    user = get_user_model().objects.filter(user_id=id)
    if len(user) == 0:
        return False
    return user[0]


def getUserByMobile(mobile=None):
    user = get_user_model().objects.filter(mobile=mobile)
    if len(user) == 0:
        return False
    return user[0]


def getUserBySchoolEmail(email, otp):
    user = get_user_model().objects.filter(email=email, otp=otp)
    if len(user) == 0:
        return False
    return user[0]


def updateUserByEmail(body, email):
    try:
        instance = get_user_model().objects.get(email=email)
        body["initial_login"] = False
        updated_instance = UserSerializer(instance, data=body)
        updated_instance.save()
        return updated_instance
    except NotFound:
        raise APIError("User not found", 400)


def updateUserById(data, id):
    try:
        instance = CustomUserModel.objects.get(user_id=id)
        body = data
        if isinstance(body, QueryDict):
            body = data.dict()
        body["initial_login"] = False
        newEmail = body.get("email")
        newMobile = body.get("mobile")
        if instance.email == newEmail or body.get("email") == "":
            body.pop("email", None)
        if instance.mobile == newMobile or body.get("mobile") == "":
            body.pop("mobile", None)

        for key in body.copy():
            if body.get(key) == "" or body.get(key) == None:
                body.pop(key, None)
        updated_instance = UserSerializer(instance, data=body)
        updated_instance.is_valid(raise_exception=True)
        updated_instance.save()
        password = body.get("password")
        if password:
            setPassword(password, id)  ## set the password after hashing of the user
        return updated_instance
    except NotFound:
        raise APIError("User not found", 400)


def setPassword(password, id=None, email=None):
    try:
        if not email:
            instance = CustomUserModel.objects.get(user_id=id)
        else:
            instance = CustomUserModel.objects.get(email=email)
        instance.set_password(password)
        instance.save()
        return True
    except Exception as e:
        print(e)
        raise APIError("Error in setting password", 500)


def checkPassword(email, password):
    print(email, password)
    try:
        user = CustomUserModel.objects.get(email=email)
        print(user)
        print(type(user))
        print('user')
        if user.check_password(password) is True:
            return user
        return False
    except Exception as e:
        print(e)
        raise APIError("Error in checking password", 500)


def createUser(data, social=False, thru_mobile=False):
    if social:
        user = UserSerializer(data=data)
        if not user.is_valid():
            raise APIError(user.errors, 401)
        user = user.create(user.validated_data)
        return user
    if thru_mobile:
        user = UserSerializer(data=data)
        if not user.is_valid():
            raise APIError(user.errors, 401)
        user = user.create(user.validated_data)
        return user

    print(data)
    temp_data = UserSerializer(data=data)
    if not temp_data.is_valid():
        raise APIError(temp_data.errors, 401)
    print(temp_data.validated_data)
    user = temp_data.create(temp_data.validated_data)
    return user


