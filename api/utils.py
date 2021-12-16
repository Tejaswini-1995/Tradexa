from django.http.response import JsonResponse
from rest_framework.views import exception_handler
from rest_framework_jwt.settings import api_settings
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import random
import smtplib
from datetime import datetime
from email.message import EmailMessage


def convert_timestamp_to_date(timestamp, option):
    if option == 'datetime':
        dt_obj = datetime.fromtimestamp(timestamp)

    return dt_obj


def generate_jwt_token(user, data):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    data["token"] = token
    return data


def generateRandom():
    return str(random.random()).split(".")[1][:4]


def parseErrors(errors):
    for i in errors:
        pass


def Error(error, code=401):
    return {"data": None, "success": False, "error": error, "status": code}


def Success(data, code=200):
    return {"data": data, "success": True, "error": None, "status": code}


# Catch only drf specific exceptions


def ErrorException(exc, context):
    HTTP_STATUS = {
        "200": "OK",
        "201": "Created",
        "202": "Accepted",
        "204": "NoContent",
        "205": "ResetContent",
        "206": "PartialContent",
        "400": "BadRequest",
        "401": "Unauthorized",
        "402": "PaymentRequired",
        "403": "Forbidden",
        "404": "NotFound",
        "405": "MethodNotAllowed",
        "406": "NotAcceptable",
        "408": "RequestTimeout",
        "409": "Conflict",
        "422": "UnprocessableEntity",
        "429": "TooManyRequests",
        "500": "ServerError",
        "501": "NotImplemented",
        "502": "BadGateway",
        "503": "ServiceUnavailable",
    }
    response = exception_handler(exc, context)
    if response is not None:
        if not response.data.get("detail"):
            response.data = list(response.data.values())[0]
            response.data = Error(response.data[0], response.status_code)
        else:
            response.data = Error(response.data["detail"], response.status_code)
        return response


class APIError(APIException):
    status_code = 400
    default_detail = "hello thre"
    default_code = "service_unavailable"
    detail = "fsdfs"

    def __init__(self, msg, code):
        self.status_code = code
        self.detail = msg


from django.http import HttpResponse
from django.conf import settings
import traceback


# Global exception handling django, drf


class ErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if settings.DEBUG:
            if exception:
                # Format your message here
                message = "**{url}**\n\n{error}\n\n````{tb}````".format(
                    url=request.build_absolute_uri(),
                    error=repr(exception),
                    tb=traceback.format_exc(),
                )
                # Do now whatever with this message
                # e.g. requests.post(<slack channel/teams channel>, data=message)
                print(message)
            return JsonResponse(Error(repr(exception), 500))


class CustomPagination(PageNumberPagination):
    page_size_query_param = 'limit'

    def get_paginated_response(self, data):
        return Response({
            "status": True,
            "code": status.HTTP_200_OK,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'data': data
        })


class SMTPEmail:
    def send_email(self, receiver, subject, message):
        try:
            gmail_user = 'diall2hiehq@gmail.com'
            gmail_pwd = 'Hiehq@Diall2'
            smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()  # extra characters to permit edit
            smtpserver.login(gmail_user, gmail_pwd)
            header = 'To:' + receiver + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: ' + subject + '\n'
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = gmail_user
            msg['To'] = receiver
            msg.set_content(message)
            # smtpserver.sendmail(gmail_user, receiver, message)
            smtpserver.send_message(msg)
            smtpserver.quit()
            return header
        except smtplib.SMTPException:

            print("Error: unable to send email")

