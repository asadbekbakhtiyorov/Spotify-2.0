from django.test import TestCase
from musicapp.models import Artist

from Spotify.musicapp.serializer import ArtistSerializer, SongSerializer


class TestArtistSerializer(TestCase):
    def setUp(self) -> None:
        pass
        self.artist1 = Artist.objects.create(
            name='Eminem',
            genre='rap',
            description='faster rap in the world'
        )

    def test_artist(self):
        a = Artist.objects.all()
        malumot = ArtistSerializer(a, many=True)
        assert malumot.data[0]['id'] == 1
        self.assertTrue(malumot.data[0]['id' == 1])
        self.assertEqual(malumot.data[0]['id'], 1)
        assert malumot.data[0]['name'] == 'Eminem'
        assert malumot.data[0]['image'] == ''

    def test_name_validation(self):
        a1 = Artist.objects.get(id=1)
        a1.name = 'Lee'
        malumot = ArtistSerializer(a1)
        assert malumot.data['name'] == 'Lee'


    def test_not_valid(self):
        artist = {
            'id':1,
            'name':'Eminem',
            'genre': 'rap',
            'description': 'The faster raper in the world'
        }
        ser = ArtistSerializer(data=artist)
        assert ser.is_valid() == False
        self.assertFalse(ser.is_valid())
        assert ser.errors['name'][0] == 'Singer with this name was absent'
        print(ser.errors)

    def test_valid(self):
        artist = {
            'id': 1,
            'name': 'Michael Jackson',
            'genre': 'Extra',
            'description': ''
        }
        ser = ArtistSerializer(data=artist)
        assert ser.is_valid() == True
        data = ser.data
        print(data)
        assert data['name'] == 'Michael Jackson'
        self.assertEqual(data['genre'], 'Extra')
        self.assertTrue(data['description'] == '')

    def test_music(self):
        music = {
            'id': 1,
            'title': 'Alfred`s theme',
            'cover': '',
            'lyrics': '',
            'album': 'Music to be murdered',
            'duration': '3:16',
            'listened': 3
        }
        ser = SongSerializer(data=music)
        assert ser.is_valid() == True
        data = ser.data
        print(data)
        assert data['title'] == 'Alfred`s Theme'
        self.assertEqual(data['duration'], 'Music to be murdered')
        self.assertTrue(data['lyrics'] == '')

    def music_not_valied(self):
        music = {
            'id': 1,
            'title': 'Alfred`s theme',
            'cover': '',
            'lyrics': '',
            'album': 'Music to be murdered',
            'duration': '3:16',
            'listened': 3
        }
        ser = SongSerializer(data=music)
        assert ser.is_valid() == False
        self.assertFalse(ser.is_valid())
        assert ser.errors['title'][0] == 'Song with this name was absent'
        print(ser.errors)