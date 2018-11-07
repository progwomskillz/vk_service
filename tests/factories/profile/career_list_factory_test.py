import unittest

from vk_service.factories.profile.career_list_factory import CareerListFactory
from vk_service.models.profile.career import Career


class CareerListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = CareerListFactory()
        self.career = {
            'group_id': 23, 'company': 'RF', 'country_id': 1, 'city_id': 1,
            'city_name': 'Moscow', 'from': 2020, 'until': 2030,
            'position': 'UpperMan'
        }
        self.values = [self.career.copy(), self.career.copy()]

    def test_factory_build(self):
        values = self.values.copy()
        careers = self.factory.build(values)
        self.assertIsInstance(careers, list)
        for i, career in enumerate(careers):
            self.assertIsInstance(career, Career)
            self.assertEqual(career.__dict__, values[i])


if __name__ == '__main__':
    unittest.main()
