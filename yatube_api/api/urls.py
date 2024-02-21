from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .constants import API_VERSION
from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comment')
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path(f'{API_VERSION}/', include('djoser.urls.jwt')),
    path(f'{API_VERSION}/', include(router.urls))
]
