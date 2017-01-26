from rest_framework.routers import DefaultRouter

from .views import IdentifierViewSet, IdentifierTypesViewSet

router = DefaultRouter()
router.register(r'identifiers', IdentifierViewSet)
router.register(r'identifiertypes', IdentifierTypesViewSet)
urlpatterns = router.urls
