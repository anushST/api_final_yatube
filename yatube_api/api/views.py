from django.shortcuts import get_object_or_404
from posts.models import Follow, Group, Post
from rest_framework import filters, mixins, permissions
from rest_framework.viewsets import (GenericViewSet, ModelViewSet,
                                     ReadOnlyModelViewSet)

from .pagination import PostLimitOffsetPagination
from .permissions import OwnerOrReadOnly, ReadOnly
from .serializers import (CommentSerializer, FollowSerializer,
                          GrouptSerializer, PostSerializer)


class BaseViewSet(ModelViewSet):
    permission_classes = (OwnerOrReadOnly,)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()


class PostViewSet(BaseViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostLimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(BaseViewSet):
    serializer_class = CommentSerializer
    pagination_class = None

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs['post_id'])

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GrouptSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = None


class ListCreateViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                        GenericViewSet):
    pass


class FollowViewSet(ListCreateViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    pagination_class = None
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
