from rest_framework.routers import DefaultRouter
from app.views import TodoViewSet, ItemViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = router.urls

