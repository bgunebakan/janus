from rest_framework.routers import DefaultRouter

from .views import ControllerViewSet

router = DefaultRouter()
router.register(r'controllers', ControllerViewSet)
urlpatterns = router.urls
