import unittest

from vk_service.factories.attachment.doc_factory import DocFactory
from vk_service.models.attachment.doc import Doc
from vk_service.models.attachment.preview import Preview


class DocFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = DocFactory()
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
        self.preview = {
            'photo': self.photo.copy(), 'graffiti': self.graffiti.copy(),
            'audio_message': self.audio_message.copy()
        }
        self.values = {
            'id': 1, 'owner_id': 53, 'title': 'MyDoc', 'size': 4566,
            'ext': 'txt', 'url': 'http://example.com/doc/', 'date': 5541552,
            'type': 1, 'preview': self.preview.copy()
        }
        self.submodels = {
            'preview': Preview
        }

    def test_factory_build(self):
        values = self.values.copy()
        doc = self.factory.build(values)
        self.assertIsInstance(doc, Doc)
        for key in self.submodels:
            values[key] = doc.__dict__[key]
        for key in self.submodels:
            self.assertIsInstance(doc.__dict__[key], self.submodels[key])
        self.assertEqual(doc.__dict__, values)


if __name__ == '__main__':
    unittest.main()
