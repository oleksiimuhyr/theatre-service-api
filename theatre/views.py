from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from theatre.models import Play
from theatre.serializers import PlaySerializer


@api_view(['GET', 'POST'])
def plays_list(request: HttpRequest) -> Response:
    if request.method == 'GET':
        movies = Play.objects.all()
        serializer = PlaySerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = PlaySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def plays_detail(request: HttpRequest, pk: int) -> Response:
    movie = get_object_or_404(Play, pk=pk)
    if request.method == 'GET':
        serializer = PlaySerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = PlaySerializer(movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
