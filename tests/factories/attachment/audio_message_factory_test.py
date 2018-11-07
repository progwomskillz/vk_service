import unittest

from vk_service.factories.attachment import AudioMessageFactory
from vk_service.models.attachment import AudioMessage


class AudioMessageFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = AudioMessageFactory()
        self.values = {
            'duration': 25,
            'waveform': [0, 5, 4, 3, 7, 2, 0],
            'link_ogg': 'http://example.com/ogg/',
            'link_mp3': 'http://example.com/mp3/'
        }

    def test_factory_build(self):
        values = self.values.copy()
        audio_message = self.factory.build(values)
        self.assertIsInstance(audio_message, AudioMessage)
        self.assertEqual(audio_message.__dict__, values)


if __name__ == '__main__':
    unittest.main()
