import unittest

from vk_service.factories.profile.military_list_factory import MilitaryListFactory
from vk_service.models.profile.military import Military


class MilitaryListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = MilitaryListFactory()
        self.military = {
            'unit': '61265', 'unit_id': 61265, 'country_id': 1, 'from': 2020,
            'until': 2021
        }
        self.values = [self.military.copy(), self.military.copy()]

    def test_factory_build(self):
        values = self.values.copy()
        militaries = self.factory.build(values)
        self.assertIsInstance(militaries, list)
        for i, military in enumerate(militaries):
            self.assertIsInstance(military, Military)
            self.assertEqual(military.__dict__, values[i])


if __name__ == '__main__':
    unittest.main()
