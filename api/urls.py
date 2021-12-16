
from django.conf.urls import include
from django.urls import path

from .auths import urls as auth_urls
from .user import urls as user_urls

from .post import urls as post_urls


urlpatterns = [
    path('auth/',include(auth_urls)),

    path('users/',include(user_urls)),

    path('post/',include(post_urls)),

]