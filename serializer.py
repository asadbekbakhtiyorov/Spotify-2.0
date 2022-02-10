from rest_framework.serializers import ModelSerializer, ValidationError
from .models import *


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'genre', 'description', 'image']

    def validated_name(self, value):
        if len(value) <= 3:
            raise ValidationError(detail='Singer with tis name was absent!')
        return value

    def validated_image(self, picture):
        if not picture.endwith ('.jbg' or '.png'):
            raise ValidationError(detail='Sorry but format of image can not to accept!')
        return picture


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'date', 'cover', 'artist']

    def validated_title(self, name):
        if len(name) <= 3:
            raise ValidationError(detail='Album with tis name was absent!')
        return name


class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'cover', 'lyrics', 'duration', 'source']

    def validated_source(self, source):
        if not source.endwith('mp3'):
            raise ValidationError(detail='Song with tis name was absent!')
        return source


