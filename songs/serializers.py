from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    album_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Song
        exclude = ["album"]

    def create(self, validated_data):
        return Song.objects.create(**validated_data)
