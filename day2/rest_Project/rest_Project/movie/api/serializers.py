from movie.models import Movie
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ['title', 'description', 'release_date']
        # read_only_fields = ['id']
        read_only_fields = ['poster']
        # exclude = ['id']
        # exclude = ['poster']