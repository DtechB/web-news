from rest_framework import routers
from .views import NewViewSet

router = routers.SimpleRouter()
router.register(r'news', NewViewSet)

urlpatterns = router.urls
