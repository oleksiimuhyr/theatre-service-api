from rest_framework import viewsets

from theatre.models import (Genre, Actor, TheatreHall,
                            Play, Performance)
from theatre.serializers import (GenreSerializer,
                                 ActorSerializer,
                                 TheatreHallSerializer,
                                 PlaySerializer,
                                 PlayListSerializer,
                                 PlayRetrieveSerializer,
                                 PerformanceSerializer,
                                 PerformanceListSerializer,
                                 PerformanceRetrieveSerializer)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class TheatreHallViewSet(viewsets.ModelViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer


class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.all()
    serializer_class = PlayListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return PlayListSerializer
        elif self.action == "retrieve":
            return PlayRetrieveSerializer
        return PlaySerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("genres", "actors")
        return queryset


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all().select_related()
    serializer_class = PerformanceSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return PerformanceListSerializer
        elif self.action == "retrieve":
            return PerformanceRetrieveSerializer
        return PerformanceSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related()

        return queryset
