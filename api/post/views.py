from django.core.exceptions import ObjectDoesNotExist
from django.http.request import QueryDict
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import action, schema
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.db.models import Prefetch

from .model import SavedPost, Post
from ..utils import APIError, Success

from .models import *
from .permissions import (

    PostViewSetPermissions,

)
from django.db.models import BooleanField, Value, Case, When, Count, IntegerField, Subquery, Q, F
from .serializers import (
   PostDetailSerializer,
    PostSerializer,

    SavedPostSerializer,
    MyPostSerializer,
    SavePostSerializer,

    UserPostDetailSerializer
)

from api.user.models import CustomUserModel


# Create your views here.


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    _serializer_classes = {


        "create": PostSerializer,
        "saved_post": SavedPostSerializer,
        "my_post": MyPostSerializer,
        "save_post": SavePostSerializer,
        "destroy": PostDetailSerializer,
    }
    permission_classes = [PostViewSetPermissions]
    lookup_field = "post_id"



    def get_queryset(self, pk=None):
        return (
            SavedPost.objects.filter(user=pk)
            if self.action == "saved_post"
            else Post.objects.filter(user=pk)
        )

    def get_serializer_class(self):
        return self._serializer_classes.get(self.action)


    def create(self, request, *args, **kwargs):
        _user_id = request.user.user_id
        post = request.data
        if isinstance(post, QueryDict):
            post = request.data.dict()
        post["user"] = _user_id
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=post)


        if not serializer.is_valid():
            raise APIError(serializer.errors, 401)
        serializer.create(serializer.validated_data)
        _user = UserPostDetailSerializer(CustomUserModel.objects.get(user_id=_user_id))
        serializer.data["userDetails"] = _user.data
        return Response(Success({"post": serializer.data}))

    @action(methods=["post"], detail=True, url_path="save-post")
    def save_post(self, request, *args, **kwargs):
        _user_id = request.user.user_id
        _post_id = kwargs.get("post_id", None)
        request.data["post"] = _post_id
        request.data["user"] = _user_id
        try:
            serializer_class = self.get_serializer_class()
            _saved_post = serializer_class(data=request.data)
            _saved_post.is_valid(raise_exception=True)
            _saved_post.create(_saved_post.validated_data)
        except:
            raise APIError("Post not found", 401)

        return Response(Success({"post": _saved_post.data}))

    @action(
        methods=["delete"],
        lookup_field="post_id",
        detail=True,
        url_path="unsave-post",
    )
    def unsave_post(self, request, *args, **kwargs):
        _user_id = request.user.user_id
        # actually post_id
        _saved_post_id = kwargs.get("post_id", None)
        try:
            _unsave_post = SavedPost.objects.get(post=_saved_post_id, user=_user_id)
            _serializer = SavedPostSerializer(_unsave_post)
            _unsave_post.delete()
        except:
            raise APIError("Saved Post Not Found", 401)
        return Response(Success(_serializer.data))

    @action(
        methods=["get"],
        detail=False,
        url_path="saved-post",
    )
    def saved_post(self, request, *args, **kwargs):
        _user_id = request.user.user_id
        _saved_post_id = kwargs.get("post_id", None)
        if _saved_post_id ==True:
            result = self.get_serializer_class()(_saved_post_id, many=True)
        return Response("Saved Post")

    def destroy(self, request, *args, **kwargs):
        _user_id = request.user.user_id
        _post_id = kwargs.get("post_id")
        print(_post_id)
        try:
            instance = Post.objects.get(post_id=_post_id)
        except:
            raise APIError("Post not found", 401)

        if instance.user.user_id != _user_id:
            raise APIError("Forbidden", 403)
        Post.objects.get(post_id=instance.post_id).delete()
        _serializer = self.get_serializer_class()(instance=instance)
        return Response(Success({"post": _serializer.data}))

