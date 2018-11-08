import unittest

from vk_service.factories.news.geo_factory import GeoFactory
from vk_service.models.news.geo import Geo


class GeoFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = GeoFactory()
        self.values = {
            'id': 1, 'title': 'RedS', 'latitude': 87, 'longitude': 178,
            'type': 'Park', 'country': 1, 'city': 1, 'address': 'RS st. 1'
        }

    def test_factory_build(self):
        values = self.values.copy()
        geo = self.factory.build(values)
        self.assertIsInstance(geo, Geo)
        self.assertEqual(geo.__dict__, values)


if __name__ == '__main__':
    unittest.main()
