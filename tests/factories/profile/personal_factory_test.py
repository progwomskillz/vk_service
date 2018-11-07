import unittest

from vk_service.factories.profile.personal_factory import PersonalFactory
from vk_service.models.profile.personal import Personal


class PersonalFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = PersonalFactory()
        self.values = {
            'political': 1, 'langs': ['rus', 'eng'], 'religion': 'Крутое',
            'inspired_by': 'Wife', 'people_main': 2, 'life_main': 1,
            'smoking': 3, 'alcohol': 3
        }

    def test_factory_build(self):
        values = self.values.copy()
        personal = self.factory.build(values)
        self.assertIsInstance(personal, Personal)
        self.assertEqual(personal.__dict__, values)


if __name__ == '__main__':
    unittest.main()
