from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'', UserViewSet)



# The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('forget-password/', forget_password, name='forget_password'),
#     path('reset-password/', reset_password, name='reset-password'),
# ]


# The API URLs are now determined automatically by the router.
urlpatterns=router.urls

