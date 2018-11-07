import unittest

from vk_service.factories.profile.universitie_list_factory import UniversitieListFactory
from vk_service.models.profile.universitie import Universitie


class UniversitieListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = UniversitieListFactory()
        self.universitie = {
            'id': 1, 'country': 1, 'city': 1, 'name': 'MGU', 'faculty': 1,
            'faculty_name': 'Fac_1', 'chair': 1, 'chair_name': 'Chair_1',
            'graduation': 2015, 'education_form': 'Ochnaya',
            'education_status': 'Выпускник (специалист)'
        }
        self.values = [self.universitie.copy(), self.universitie.copy()]

    def test_factory_build(self):
        values = self.values.copy()
        universities = self.factory.build(values)
        self.assertIsInstance(universities, list)
        for i, universitie in enumerate(universities):
            self.assertIsInstance(universitie, Universitie)
            self.assertEqual(universitie.__dict__, values[i])


if __name__ == '__main__':
    unittest.main()
