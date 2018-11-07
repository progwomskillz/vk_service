import unittest

from vk_service.factories.profile.city_factory import CityFactory
from vk_service.models.profile.city import City


class CityFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = CityFactory()
        self.values = {'id': 1, 'title': 'Moscow'}

    def test_factory_build(self):
        values = self.values.copy()
        city = self.factory.build(values)
        self.assertIsInstance(city, City)
        self.assertEqual(city.__dict__, values)


if __name__ == '__main__':
    unittest.main()
