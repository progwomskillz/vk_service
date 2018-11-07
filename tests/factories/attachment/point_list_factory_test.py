import unittest

from vk_service.factories.attachment.point_list_factory import PointListFactory
from vk_service.models.attachment.point import Point


class PointListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = PointListFactory()
        self.point = {'position': 1, 'color': 'FFFFFF'}
        self.values = [self.point.copy(), self.point.copy(), self.point.copy()]

    def test_factory_build(self):
        values = self.values.copy()
        points = self.factory.build(values)
        self.assertIsInstance(points, list)
        for i, point in enumerate(points):
            self.assertIsInstance(point, Point)
            self.assertEqual(point.__dict__, values[i])


if __name__ == '__main__':
    unittest.main()
