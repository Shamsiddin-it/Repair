from rest_framework.routers import DefaultRouter
from .views import WorkerProfileViewSet

router = DefaultRouter()
router.register(r'profiles', WorkerProfileViewSet)

urlpatterns = router.urls
