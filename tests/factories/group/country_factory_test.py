import unittest

from vk_service.factories.group.country_factory import CountryFactory
from vk_service.models.group.country import Country


class CountryFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = CountryFactory()
        self.values = {'id': 1, 'title': 'Russia'}

    def test_factory_build(self):
        values = self.values.copy()
        country = self.factory.build(values)
        self.assertIsInstance(country, Country)
        self.assertEqual(country.__dict__, values)


if __name__ == '__main__':
    unittest.main()
