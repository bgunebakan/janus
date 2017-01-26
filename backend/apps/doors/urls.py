from rest_framework.routers import DefaultRouter

from .views import DoorViewSet

router = DefaultRouter()
router.register(r'doors', DoorViewSet)
urlpatterns = router.urls
