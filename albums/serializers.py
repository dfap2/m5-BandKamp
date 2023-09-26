from users.serializers import UserSerializer
from rest_framework import serializers
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Album
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        return Album.objects.create(**validated_data)
