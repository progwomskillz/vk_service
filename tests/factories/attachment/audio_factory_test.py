import unittest

from vk_service.factories.attachment import AudioFactory
from vk_service.models.attachment import Audio


class AudioFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = AudioFactory()
        self.values = {
            'id': 25, 'owner_id': 53, 'artist': 'Pentatonix', 'title': 'Moon',
            'duration': 250, 'url': 'http://example.com/mp3/', 'lyrics_id': 2,
            'album_id': 5, 'genre_id': 1, 'date': 25252151, 'no_search': 1,
            'is_hq': 1
        }

    def test_factory_build(self):
        values = self.values.copy()
        audio = self.factory.build(values)
        self.assertIsInstance(audio, Audio)
        self.assertEqual(audio.__dict__, values)


if __name__ == '__main__':
    unittest.main()
