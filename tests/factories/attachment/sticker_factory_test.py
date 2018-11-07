import unittest

from vk_service.factories.attachment.sticker_factory import StickerFactory
from vk_service.models.attachment.sticker import Sticker
from vk_service.models.attachment.image import Image


class StickerFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = StickerFactory()
        self.image = {
            'src': 'http://example.com/m.jpg', 'width': 130,
            'height': 87, 'type': 'm'
        }
        self.images = [self.image.copy(), self.image.copy(), self.image.copy()]
        self.image_with_background = {
            'src': 'http://example.com/m.jpg', 'width': 130,
            'height': 87, 'type': 'm'
        }
        self.images_with_background = [
            self.image_with_background.copy(),
            self.image_with_background.copy()
        ]
        self.values = {
            'product_id': 10, 'sticker_id': 2, 'images': self.images.copy(),
            'images_with_background': self.images_with_background.copy()
        }
        self.submodels = {
            'images': Image,
            'images_with_background': Image
        }

    def test_factory_build(self):
        values = self.values.copy()
        sticker = self.factory.build(values)
        self.assertIsInstance(sticker, Sticker)
        for key in self.submodels:
            values[key] = sticker.__dict__[key]
        for key in self.submodels:
            for item in sticker.__dict__[key]:
                self.assertIsInstance(item, self.submodels[key])
        self.assertEqual(sticker.__dict__, values)


if __name__ == '__main__':
    unittest.main()
