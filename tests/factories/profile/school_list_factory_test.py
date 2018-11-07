import unittest

from vk_service.factories.profile.school_list_factory import SchoolListFactory
from vk_service.models.profile.school import School


class SchoolListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = SchoolListFactory()
        self.school = {
            'id': 2, 'country': 1, 'city': 1, 'name': 'SOSH2',
            'year_from': 2007, 'year_to': 2011, 'year_graduated': 2011,
            'class': 'B', 'speciality': 'None', 'type': 1,
            'type_str': 'школа'
        }
        self.values = [self.school.copy(), self.school.copy()]

    def test_factory_build(self):
        values = self.values.copy()
        schools = self.factory.build(values)
        self.assertIsInstance(schools, list)
        for i, school in enumerate(schools):
            self.assertIsInstance(school, School)
            self.assertEqual(school.__dict__, values[i])


if __name__ == '__main__':
    unittest.main()
