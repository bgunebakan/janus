from rest_framework.routers import DefaultRouter

from .views import PermissionViewSet, PermissionTypesViewSet

router = DefaultRouter()
router.register(r'permissions', PermissionViewSet)
router.register(r'permissiontypes', PermissionTypesViewSet)
urlpatterns = router.urls
