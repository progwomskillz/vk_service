import unittest

from vk_service.factories.profile.profile_list_factory import ProfileListFactory
from vk_service.models.profile.profile import Profile
from vk_service.models.profile.career import Career
from vk_service.models.profile.city import City
from vk_service.models.profile.counter import Counter
from vk_service.models.profile.country import Country
from vk_service.models.profile.crop_photo import CropPhoto
from vk_service.models.profile.last_seen import LastSeen
from vk_service.models.profile.military import Military
from vk_service.models.profile.occupation import Occupation
from vk_service.models.profile.personal import Personal
from vk_service.models.profile.relative import Relative
from vk_service.models.profile.school import School
from vk_service.models.profile.universitie import Universitie


class ProfileListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = ProfileListFactory()
        self.career_dict = {
            'group_id': 23, 'company': 'RF', 'country_id': 1, 'city_id': 1,
            'city_name': 'Moscow', 'from': 2020, 'until': 2030,
            'position': 'UpperMan'
        }
        self.career = [self.career_dict.copy(), self.career_dict.copy()]
        self.city = {'id': 1, 'title': 'Moscow'}
        self.counters = {
            'albums': 1, 'videos': 0, 'audios': 3, 'photos': 15, 'notes': 0,
            'friends': 152, 'groups': 1474, 'online_friends': 5,
            'mutual_friends': 1, 'user_videos': 0, 'followers': 251,
            'pages': 54
        }
        self.country = {'id': 1, 'title': 'Russia'}
        self.photo = {'id': 5}
        self.crop = {'x': 1, 'y': 1, 'x2': 99, 'y2': 99}
        self.rect = {'x': 1, 'y': 1, 'x2': 99, 'y2': 99}
        self.crop_photo = {
            'photo': self.photo.copy(),
            'crop': self.crop.copy(),
            'rect': self.rect.copy()
        }
        self.last_seen = {'time': 51561265, 'platform': 1}
        self.military_dict = {
            'unit': '61265', 'unit_id': 61265, 'country_id': 1, 'from': 2020,
            'until': 2021
        }
        self.military = [self.military_dict.copy(), self.military_dict.copy()]
        self.occupation = {'type': 'school', 'id': 1, 'name': 'SOSH1'}
        self.personal = {
            'political': 1, 'langs': ['rus', 'eng'], 'religion': 'Крутое',
            'inspired_by': 'Wife', 'people_main': 2, 'life_main': 1,
            'smoking': 3, 'alcohol': 3
        }
        self.relative = {'id': 5, 'name': 'Валентина', 'type': 'parent'}
        self.relatives = [self.relative.copy(), self.relative.copy()]
        self.school = {
            'id': 2, 'country': 1, 'city': 1, 'name': 'SOSH2',
            'year_from': 2007, 'year_to': 2011, 'year_graduated': 2011,
            'class': 'B', 'speciality': 'None', 'type': 1,
            'type_str': 'школа'
        }
        self.schools = [self.school.copy(), self.school.copy()]
        self.universitie = {
            'id': 1, 'country': 1, 'city': 1, 'name': 'MGU', 'faculty': 1,
            'faculty_name': 'Fac_1', 'chair': 1, 'chair_name': 'Chair_1',
            'graduation': 2015, 'education_form': 'Ochnaya',
            'education_status': 'Выпускник (специалист)'
        }
        self.universities = [self.universitie.copy(), self.universitie.copy()]
        self.profile = {
            'id': 43, 'first_name': 'Alex', 'last_name': 'Mikel',
            'career': self.career.copy(),
            'city': self.city.copy(),
            'counters': self.counters.copy(),
            'country': self.country.copy(),
            'crop_photo': self.crop_photo.copy(),
            'last_seen': self.last_seen.copy(),
            'military': self.military.copy(),
            'occupation': self.occupation.copy(),
            'personal': self.personal.copy(),
            'relatives': self.relatives.copy(),
            'schools': self.schools.copy(),
            'universities': self.universities.copy()
        }
        self.values = [self.profile.copy(), self.profile.copy()]
        self.submodels = {
            'career': Career,
            'city': City,
            'counters': Counter,
            'country': Country,
            'crop_photo': CropPhoto,
            'last_seen': LastSeen,
            'military': Military,
            'occupation': Occupation,
            'personal': Personal,
            'relatives': Relative,
            'schools': School,
            'universities': Universitie,
        }

    def test_factory_build(self):
        values = self.values.copy()
        profiles = self.factory.build(values)
        self.assertIsInstance(profiles, list)
        for i, profile in enumerate(profiles):
            self.assertIsInstance(profile, Profile)
            for key in self.submodels:
                values[i][key] = profile.__dict__[key]
            for key in self.submodels:
                value = self.submodels[key]
                if isinstance(profile.__dict__[key], list):
                    for item in profile.__dict__[key]:
                        self.assertIsInstance(item, value)
                else:
                    self.assertIsInstance(profile.__dict__[key], value)
            self.assertEqual(profile.__dict__, values[i])


if __name__ == '__main__':
    unittest.main()
