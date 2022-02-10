from unittest import TestCase
from musicapp.models import Artist, Song, Album
from musicapp.serializer import ArtistSerializer, SongSerializer, AlbumSerializer
from django.test import client


class TestArtistViewSet(TestCase):
    def setUp(self) -> None:
        cl = client()

    def test_get_artist(self):
        natija = self.cl.get('/album/')
        assert natija.status_code == 200
        m = natija.data
        print(m)
        ArtistSerializer(natija.data)
        self.assertTrue(len(m) != 0)
        self.assertEqual(m['name'], "Jahongir Otajonov")
        self.assertEqual(m["genre"], 'Classic')

    def test_album(self):
        natija = self.cl.get('/album/')
        assert natija.status_code == 200
        m = natija.data
        print(m)
        self.assertTrue(len(m) != 0)
        self.assertEqual(m['title'], "Music to be murdered")
        self.assertEqual(m['genre'], "Rap")