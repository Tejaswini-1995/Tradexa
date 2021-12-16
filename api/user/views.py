from django.http.request import QueryDict
from api.user.services import updateUserById, getUserByMobile
from rest_framework import viewsets
from rest_framework.response import Response

from .models import CustomUserModel
from .serializers import UserDetailSerializer, UserSerializer
from ..otp.serializers import OTPSerializer

from ..utils import APIError, Success, generateRandom, SMTPEmail, Error
from django.contrib.auth import get_user_model, authenticate
from .permissions import UserViewSetPermissions
from ..otp.services import sendOTP, verifyOTP
from rest_framework.parsers import JSONParser, MultiPartParser

from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny
from rest_framework import permissions, status
import os
import stripe


from ..otp.models import OTP


# Create your views here.


class UpdateModelMixin(object):
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # refresh the instance from the database.
            instance = self.get_object()
            serializer = self.get_serializer(instance)

        return Response(Success({"user": serializer.data}))

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    parser_classes = [JSONParser, MultiPartParser]
    serializer_class = UserSerializer
    serializer_classes = {
        "partial_update": UserSerializer,
        "update": UserSerializer,
        "retrieve": UserDetailSerializer,
    }
    queryset = get_user_model().objects.all()
    permission_classes = [UserViewSetPermissions]
    lookup_field = "user_id"

    def get_serializer_class(self):
        return self.serializer_classes[self.action]

    def _check_for_onboarding(self, user_id):
        is_onboarded = False
        user = CustomUserModel.objects.get(user_id=user_id)
        if user.email and user.full_name and user.date_of_birth:
            if user.is_school:
                is_onboarded = True  # school
            elif user.mobile:
                is_onboarded = True
        newData = {"is_onboarded": is_onboarded}
        updated_user = updateUserById(newData, user_id)
        return updated_user

    def partial_update(self, request, *args, **kwargs):
        if not request.user.user_id == int(kwargs["user_id"]):
            raise APIError("Unauthorized Request", 400)
        body = request.data
        if isinstance(request.data, QueryDict):
            body = request.data.dict()
        mobile = None
        tempMobile = body.get("mobile")
        if tempMobile:
            mobile = tempMobile[len(tempMobile) - 10:]
        otp = body.get("otp")
        if mobile and mobile == request.user.mobile:
            tempMobile = None
            print(tempMobile)
            body.pop("mobile")
            otp = None
        updated_user = None
        if tempMobile and not otp:
            if getUserByMobile(mobile):
                raise APIError('Mobile is aleady taken', 401)
            sendOTP(tempMobile)
            otp = OTP.objects.filter(mobile=tempMobile[3:])
            print(otp[0])
            return Response(Success({"status": f"OTP sent to {tempMobile}", "otp": otp[0].otp}))
        if tempMobile and otp:
            if not verifyOTP(tempMobile, otp):
                raise APIError('OTP did not match', 401)
            mobile = tempMobile[len(tempMobile) - 10:]
            newData = {"mobile": mobile}
            updated_user = updateUserById(newData, request.user.user_id)
        else:
            updated_user = updateUserById(body, request.user.user_id)

        # check is all the required info exist, if yes then set is_onboarded to true
        updated_user = self._check_for_onboarding(request.user.user_id)
        return Response(Success({"user": updated_user.data}))

    def retrieve(self, request, *args, **kwargs):
        if not request.user.user_id == int(kwargs["user_id"]):
            raise APIError("Unauthorized Request", 400)
        instance = self.get_object()
        serializer = self.get_serializer_class()(instance)
        return Response(Success({"user": serializer.data}))


    def forget_password(self, request):
        email_id = request.data.get('email')
        otp = request.data.get('otp')

        if otp is not None:
            if CustomUserModel.objects.filter(email=email_id, otp=otp).exists():
                return Response(Success('OTP verified successfully', 200))
            else:
                return Response(Error('Incorrect OTP', 400))
        try:
            userDetails = CustomUserModel.objects.get(email=request.data.get('email'))
            custom_otp = generateRandom()
            otp = str(custom_otp)

            userData = UserDetailSerializer(userDetails, {'otp': otp})
            if userData.is_valid():
                subject = "Reset Password"
                message = 'You have requested to reset your password\n' \
                          'Your OTP for reset password is : ' + otp + '\n'

                SMTPEmail.send_email(SMTPEmail, email_id, subject, message)
                userData.save()
            else:
                return Response(userData.errors, status=status.HTTP_200_OK)
        except:
            return Response(Error('User not found.', 400))

        return Response(Success('OTP sent to email', 200))

    @action(
        detail=False,
        methods=["POST"],
        url_path="reset-password",
    )
    def reset_password(self, request):
        body = request.data
        email = request.data.get('email')

        try:

            userDetails = CustomUserModel.objects.get(email=email)

            if not userDetails:
                return Response(Error('Please check Email ID.', 400))

            userDetails.set_password(body['password'])
            userDetails.save()
            user = UserDetailSerializer(userDetails)

            return Response(Success('Reset Password successful.', 200))

        except:
            return Response(Error('Please check Email ID.', 400))

