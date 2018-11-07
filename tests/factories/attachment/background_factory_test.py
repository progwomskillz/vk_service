import unittest

from vk_service.factories.attachment.background_factory import BackgroundFactory
from vk_service.models.attachment.background import Background
from vk_service.models.attachment.point import Point
from vk_service.models.attachment.image import Image


class BackgroundFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = BackgroundFactory()
        self.point = {'position': 1, 'color': 'FFFFFF'}
        self.points = [self.point.copy(), self.point.copy(), self.point.copy()]
        self.values_1 = {
            'id': 25, 'type': 'gradient', 'angle': 48, 'color': 'FFFFFF',
            'points': self.points.copy()
        }
        self.submodels_1 = {
            'points': Point
        }
        self.image = {
            'src': 'http://example.com/m.jpg', 'width': 130,
            'height': 87, 'type': 'm'
        }
        self.images = [self.image.copy(), self.image.copy(), self.image.copy()]
        self.values_2 = {
            'id': 26, 'type': 'tile', 'color': 'FFFFFF', 'width': 580,
            'height': 220, 'images': self.images.copy()
        }
        self.submodels_2 = {
            'images': Image
        }

    def test_factory_build(self):
        values = self.values_1.copy()
        background = self.factory.build(values)
        self.assertIsInstance(background, Background)
        for key in self.submodels_1:
            values[key] = background.__dict__[key]
        for key in self.submodels_1:
            for item in background.__dict__[key]:
                self.assertIsInstance(item, self.submodels_1[key])
        self.assertEqual(background.__dict__, values)

        values = self.values_2.copy()
        background = self.factory.build(values)
        self.assertIsInstance(background, Background)
        for key in self.submodels_2:
            values[key] = background.__dict__[key]
        for key in self.submodels_2:
            for item in background.__dict__[key]:
                self.assertIsInstance(item, self.submodels_2[key])
        self.assertEqual(background.__dict__, values)


if __name__ == '__main__':
    unittest.main()
