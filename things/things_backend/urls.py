from rest_framework.routers import SimpleRouter

from .views import CategoryViewSet, PostViewSet, TagViewSet

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('tags', TagViewSet)
router.register('categories', CategoryViewSet)
