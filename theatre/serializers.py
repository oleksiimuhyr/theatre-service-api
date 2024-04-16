from rest_framework import serializers
from theatre.models import (Play, Genre,
                            Actor, TheatreHall)


class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ("id", "title", "description")

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField(max_length=255)

    def create(self: Play, validated_data: dict) -> Play:
        return Play.objects.create(**validated_data)

    def update(self: Play, instance: Play.objects,
               validated_data: dict) -> Play:
        instance.title = validated_data.get('title', instance)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.save()
        return instance


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")

    name = serializers.CharField(max_length=100, required=True)

    def create(self: Genre, validated_data: dict) -> Genre:
        return Genre.objects.create(**validated_data)

    def update(self: Genre, instance: Genre.objects,
               validated_data: dict) -> Genre:
        instance.name = validated_data.get('name', instance)
        instance.save()
        return instance


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")

    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

    def create(self: Actor, validated_data: dict) -> Actor:
        return Actor.objects.create(**validated_data)

    def update(self: Actor, instance:Actor.objects,
               validated_data: dict) -> Actor:
        instance.first_name = validated_data.get('first_name', instance)
        instance.last_name = validated_data.get('last_name', instance)
        instance.save()
        return instance


class TheatreHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = ("id", "name", "rows", "seats_in_row")

    name = serializers.CharField(max_length=255)
    rows = serializers.IntegerField()
    seats_in_row = serializers.IntegerField()

    def create(self: TheatreHall, validated_data: dict) -> TheatreHall:
        return TheatreHall.objects.create(**validated_data)

    def update(self: TheatreHall, instance: TheatreHall.objects,
               validated_data: dict) -> TheatreHall:
        instance.name = validated_data.get('name', instance)
        instance.rows = validated_data.get('rows', instance)
        instance.seats_in_row = validated_data.get('seats_in_row', instance)
        instance.save()
        return instance
