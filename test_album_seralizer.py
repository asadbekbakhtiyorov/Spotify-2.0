from django.test import TestCase

from Spotify.musicapp.models import Album
from Spotify.musicapp.serializer import AlbumSerializer


class TestAlbumSerializer(TestCase):
    def setUp(self) -> None:
        pass

    def test_album_title(self):
        a = Album.objects.all()
        malumot = AlbumSerializer(a)
        assert malumot.data['title'] == 'Music To Be Murdered By'

    def test_album_data(self):
        a = Album.objects.all()
        malumot = AlbumSerializer(a)
        assert malumot.data['date'] == '20.12.2019'

    def test_album_artist(self):
        a1 = Album.objects.get(id=1)
        a1.name = 'Eminem'
        malumot = AlbumSerializer(a1)
        assert malumot.data['name'] == 'Eminem'

