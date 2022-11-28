from rest_framework.routers import SimpleRouter

from .views import UserProfileViewSet


router = SimpleRouter()
router.register('users', UserProfileViewSet)