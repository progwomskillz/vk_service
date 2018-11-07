import unittest

from vk_service.factories.attachment.image_list_factory import ImageListFactory
from vk_service.models.attachment.image import Image


class ImageListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = ImageListFactory()
        self.image = {
            'src': 'http://example.com/m.jpg', 'width': 130, 'height': 87,
            'type': 'm'
        }
        self.values = [self.image.copy(), self.image.copy(), self.image.copy()]

    def test_factory_build(self):
        values = self.values.copy()
        images = self.factory.build(values)
        self.assertIsInstance(images, list)
        for i, image in enumerate(images):
            self.assertIsInstance(image, Image)
            self.assertEqual(image.__dict__, values[i])


if __name__ == '__main__':
    unittest.main()
