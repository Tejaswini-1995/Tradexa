from api.user.models import CustomUserModel
from rest_framework import serializers
from .models import Post, SavedPost
from .services import *




class UserPostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ("user_id", "first_name")

    depth = 1


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "user",
            "post_id",

            "post_title",
            "post_content",

        )



    depth = 1




class PostDetailSerializer(serializers.ModelSerializer):

    user = UserPostDetailSerializer()

    class Meta:
        model = Post
        fields = [
            "user",
            "post_id",
            "post_content",
            "post_title",

            "created_at",
        ]
        depth = 1



class SavedPostSerializer(serializers.ModelSerializer):




    def create(self, validated_data):
        return SavedPost.objects.create(**validated_data)

    class Meta:
        model = SavedPost
        fields = ("post")

    depth = 1


class SavePostSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return SavedPost.objects.get_or_create(**validated_data)

    class Meta:
        model = SavedPost
        fields = (
            "post",
            "user",
            "saved_post_id",
        )


class MyPostSerializer(serializers.ModelSerializer):

    user = UserPostDetailSerializer()


    class Meta:
        model = Post
        fields = [

            "user",
            "post_id",
            "post_title",

            "created_at",
        ]
        depth = 1
