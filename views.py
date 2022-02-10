from django.contrib.postgres.search import TrigramSimilarity
from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *


# Create your views here.


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    pagination_class = [LimitOffsetPagination]

    def get_queryset(self):
        artist = Artist.objects.all()
        word = self.request.query_params.get('search')
        if word is not None:
            artist = Artist.objects.annotate(
                similarity=TrigramSimilarity('name', word)
            ).filter(similarity__gte=0.5).order_by('-similarity')
            return artist

    @action(detail=True, methods=['GET', 'POST'])
    def artist(self, request, *args, **kwards):
        artist = self.get_object()
        al = Album.objects.filter(artist=artist)
        ser = AlbumSerializer(al, many=True)
        return Response(ser.data)

    @action(detail=True, methods=['GET', 'POST'])
    def album(self, request, *args, **kwards):
        artist = self.get_object()
        al = request.datd
        ser = AlbumSerializer(data=al, many=True)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = [OrderingFilter,]
    ordering_fields = ['date']

    @action(detail=True, methods=['GET'])
    def albums(self, request, *args, **kwards):
        album = self.get_object()
        sn = Song.objects.filter(album=album)
        ser = SongSerializer(sn, many=True)
        return Response(ser.data)


class SongViewsSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    @action(detail=True, methods=['GET'])
    def albums(self, request, *args, **kwards):
        song = self.get_object()
        sn = Album.objects.filter(id=song.album.id)
        ser = AlbumSerializer(sn, many=True)
        return Response(ser.data)

    @action(detail=True, methods=['GET'])
    def albums(self, request, *args, **kwards):
        song = self.get_object()
        sn = Album.objects.filter(id=song.album.id)
        ser = AlbumSerializer(sn, many=True)
        return Response(ser.data)