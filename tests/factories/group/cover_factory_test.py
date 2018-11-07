import unittest

from vk_service.factories.group.cover_factory import CoverFactory
from vk_service.models.group.cover import Cover
from vk_service.models.group.image import Image


class CoverFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = CoverFactory()
        self.image = {
            'src': 'http://example.com/m.jpg', 'width': 130, 'height': 87,
            'type': 'm'
        }
        self.images = [self.image.copy(), self.image.copy(), self.image.copy()]
        self.values = {'enabled': 1, 'images': self.images.copy()}
        self.submodels = {
            'images': Image
        }

    def test_factory_build(self):
        values = self.values.copy()
        cover = self.factory.build(values)
        self.assertIsInstance(cover, Cover)
        for key in self.submodels:
            values[key] = cover.__dict__[key]
        for key in self.submodels:
            for item in cover.__dict__[key]:
                self.assertIsInstance(item, self.submodels[key])
        self.assertEqual(cover.__dict__, values)


if __name__ == '__main__':
    unittest.main()
