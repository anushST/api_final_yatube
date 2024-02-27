from django.shortcuts import get_object_or_404
from posts.models import Follow, Group, Post
from rest_framework import filters, mixins, permissions
from rest_framework.viewsets import (GenericViewSet, ModelViewSet,
                                     ReadOnlyModelViewSet)

from .permissions import OwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer,
                          GrouptSerializer, PostSerializer)


class BaseViewSet(ModelViewSet):
    permission_classes = (OwnerOrReadOnly,)


class PostViewSet(BaseViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        if not self.request.query_params:
            self.pagination_class = None
        return super().get_queryset()

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
    pagination_class = None


class ListCreateViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                        GenericViewSet):
    pass


class FollowViewSet(ListCreateViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = None
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
