from theatre.views import (GenreViewSet, ActorViewSet, TheatreHallViewSet,
                           PlayViewSet, PerformanceViewSet)
from rest_framework import routers

router = routers.DefaultRouter()
router.register("/genres", GenreViewSet)
router.register("/actors", ActorViewSet)
router.register("/theatre_halls", TheatreHallViewSet)
router.register("/plays", PlayViewSet)
router.register("/performances", PerformanceViewSet)

app_name = "theatre"

urlpatterns = router.urls
