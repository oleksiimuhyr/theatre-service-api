from rest_framework import serializers
from theatre.models import Play


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
