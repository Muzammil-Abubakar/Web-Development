from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, AuthorViewSet, TagViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
