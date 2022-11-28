from rest_framework.routers import SimpleRouter

from .views import PostViewSet, TagViewSet, CategoryViewSet

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('tags', TagViewSet)
router.register('categories', CategoryViewSet)
