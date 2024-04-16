from django.urls import path, include
from theatre.views import (GenreList, GenreDetail,
                          ActorList, ActorDetail,
                          TheatreHallViewSet, PlayViewSet)
from rest_framework import routers

router = routers.DefaultRouter()

router.register("/plays", PlayViewSet)

theatre_halls_list = TheatreHallViewSet.as_view(
    actions={"get": "list", "post": "create"}
)

theatre_halls_detail = TheatreHallViewSet.as_view(
    actions={"get": "retrieve",
             "put": "update",
             "delete": "destroy",
             "patch": "partial_update"}
)


urlpatterns = [
    path("/genres/", GenreList.as_view(), name="genres-list"),
    path("/genres/<int:pk>/", GenreDetail.as_view(), name="genres-detail"),
    path("/actors/", ActorList.as_view(), name="actors-list"),
    path("/actors/<int:pk>/", ActorDetail.as_view(), name="actors-detail"),
    path("/theatre_halls/", theatre_halls_list, name="theatre_halls-list"),
    path("/theatre_halls/<int:pk>/", theatre_halls_detail,
         name="theatre_halls-detail"),
    path("", include(router.urls)),
]

app_name = "theatre"
