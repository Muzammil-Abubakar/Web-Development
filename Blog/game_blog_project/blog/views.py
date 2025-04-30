from rest_framework import viewsets, filters
from .models import Post, Author, Tag
from .serializers import (
    PostReadSerializer,
    PostWriteSerializer,
    AuthorSerializer,
    TagSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-published_at')
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ['published_at']

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-published_at')
        tag = self.request.query_params.get('tags', None)
        if tag:
            queryset = queryset.filter(tags__name=tag)
        return queryset

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PostReadSerializer
        return PostWriteSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
