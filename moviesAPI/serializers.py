from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields = ('id', 'person', 'name', 'desc', 'created_at', 'updated_at')