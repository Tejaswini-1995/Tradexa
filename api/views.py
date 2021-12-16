from django.shortcuts import render
from django.core import exceptions
from rest_framework.response import Response
from .utils import APIError, Error
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

@api_view()
@renderer_classes([JSONRenderer])
def error_404(request,format=None):
    print(request.method)
    # raise APIError('No',400)
    return Response(Error('Not found',404))
# Create your views here.
