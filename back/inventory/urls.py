from rest_framework import routers

from .views import InventoryViewSet

router = routers.SimpleRouter()
router.register(r"", InventoryViewSet, basename="inventory")
urlpatterns = router.urls
