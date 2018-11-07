import unittest

from vk_service.factories.attachment.preview_factory import PreviewFactory
from vk_service.models.attachment.preview import Preview
from vk_service.models.attachment.photo import Photo
from vk_service.models.attachment.graffiti import Graffiti
from vk_service.models.attachment.audio_message import AudioMessage


class PreviewFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = PreviewFactory()
        self.size = {
            'src': 'http://example.com/m.jpg', 'width': 130,
            'height': 87, 'type': 'm'
        }
        self.sizes = [self.size.copy(), self.size.copy(), self.size.copy()]
        self.photo = {'sizes': self.sizes.copy()}
        self.graffiti = {
            'src': 'http://example.com/graffiti',
            'width': 588, 'height': 551
        }
        self.audio_message = {
            'duration': 25,
            'waveform': [0, 5, 4, 3, 7, 2, 0],
            'link_ogg': 'http://example.com/ogg/',
            'link_mp3': 'http://example.com/mp3/'
        }
        self.values = {
            'photo': self.photo.copy(), 'graffiti': self.graffiti.copy(),
            'audio_message': self.audio_message.copy()
        }
        self.submodels = {
            'photo': Photo,
            'graffiti': Graffiti,
            'audio_message': AudioMessage
        }

    def test_factory_build(self):
        values = self.values.copy()
        preview = self.factory.build(values)
        self.assertIsInstance(preview, Preview)
        for key in self.submodels:
            values[key] = preview.__dict__[key]
        for key in self.submodels:
            self.assertIsInstance(preview.__dict__[key], self.submodels[key])
        self.assertEqual(preview.__dict__, values)


if __name__ == '__main__':
    unittest.main()
