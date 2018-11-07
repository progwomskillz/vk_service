from .profile_info import ProfileInfo
from vk_service.factories.profile.career_list_factory import CareerListFactory
from vk_service.factories.profile.city_factory import CityFactory
from vk_service.factories.profile.counter_factory import CounterFactory
from vk_service.factories.profile.country_factory import CountryFactory
from vk_service.factories.profile.crop_photo_factory import CropPhotoFactory
from vk_service.factories.profile.last_seen_factory import LastSeenFactory
from vk_service.factories.profile.military_list_factory import MilitaryListFactory
from vk_service.factories.profile.occupation_factory import OccupationFactory
from vk_service.factories.profile.personal_factory import PersonalFactory
from vk_service.factories.profile.relative_list_factory import RelativeListFactory
from vk_service.factories.profile.school_list_factory import SchoolListFactory
from vk_service.factories.profile.universitie_list_factory import UniversitieListFactory


class Profile(ProfileInfo):
    def __init__(self, values):
        factories = {
            'career': CareerListFactory(),
            'city': CityFactory(),
            'counters': CounterFactory(),
            'country': CountryFactory(),
            'crop_photo': CropPhotoFactory(),
            'last_seen': LastSeenFactory(),
            'military': MilitaryListFactory(),
            'occupation': OccupationFactory(),
            'personal': PersonalFactory(),
            'relatives': RelativeListFactory(),
            'schools': SchoolListFactory(),
            'universities': UniversitieListFactory()
        }
        super(Profile, self).__init__(values, factories)
