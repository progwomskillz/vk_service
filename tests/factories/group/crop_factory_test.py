import unittest

from vk_service.factories.group.crop_factory import CropFactory
from vk_service.models.group.crop import Crop


class CropFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = CropFactory()
        self.values = {'x': 1, 'y': 1, 'x2': 99, 'y2': 99}

    def test_factory_build(self):
        values = self.values.copy()
        crop = self.factory.build(values)
        self.assertIsInstance(crop, Crop)
        self.assertEqual(crop.__dict__, values)


if __name__ == '__main__':
    unittest.main()
