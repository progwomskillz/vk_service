import unittest

from vk_service.factories.group.rect_factory import RectFactory
from vk_service.models.group.rect import Rect


class RectFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = RectFactory()
        self.values = {'x': 1, 'y': 1, 'x2': 99, 'y2': 99}

    def test_factory_build(self):
        values = self.values.copy()
        rect = self.factory.build(values)
        self.assertIsInstance(rect, Rect)
        self.assertEqual(rect.__dict__, values)


if __name__ == '__main__':
    unittest.main()
