import unittest

from vk_service.factories.profile.occupation_factory import OccupationFactory
from vk_service.models.profile.occupation import Occupation


class OccupationFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = OccupationFactory()
        self.values = {'type': 'school', 'id': 1, 'name': 'SOSH1'}

    def test_factory_build(self):
        values = self.values.copy()
        occupation = self.factory.build(values)
        self.assertIsInstance(occupation, Occupation)
        self.assertEqual(occupation.__dict__, values)


if __name__ == '__main__':
    unittest.main()
