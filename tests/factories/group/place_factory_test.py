import unittest

from vk_service.factories.group.place_factory import PlaceFactory
from vk_service.models.group.place import Place


class PlaceFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = PlaceFactory()
        self.values = {
            'id': 1, 'title': 'RedS', 'latitude': 87, 'longitude': 178,
            'type': 'Park', 'country': 1, 'city': 1, 'address': 'RS st. 1'
        }

    def test_factory_build(self):
        values = self.values.copy()
        place = self.factory.build(values)
        self.assertIsInstance(place, Place)
        self.assertEqual(place.__dict__, values)


if __name__ == '__main__':
    unittest.main()
