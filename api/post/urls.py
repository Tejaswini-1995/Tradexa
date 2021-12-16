from django.urls.conf import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import  PostViewSet

router = SimpleRouter()
router.register("post", PostViewSet)
router.register("post/<int:post_id>/save-post",PostViewSet)
router.register("post/<int:saved_post_id>/unsave-post",PostViewSet)
router.register("post/saved-post",PostViewSet)
router.register("post/my-post",PostViewSet)



urlpatterns = [
    path(r"", include(router.urls)),
]