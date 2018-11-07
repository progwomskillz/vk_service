from .group_info import GroupInfo
from vk_service.factories.group.ban_factory import BanFactory
from vk_service.factories.group.city_factory import CityFactory
from vk_service.factories.group.contact_list_factory import ContactListFactory
from vk_service.factories.group.counter_factory import CounterFactory
from vk_service.factories.group.country_factory import CountryFactory
from vk_service.factories.group.cover_factory import CoverFactory
from vk_service.factories.group.crop_photo_factory import CropPhotoFactory
from vk_service.factories.group.link_list_factory import LinkListFactory
from vk_service.factories.group.market_factory import MarketFactory
from vk_service.factories.group.place_factory import PlaceFactory


class Group(GroupInfo):
    def __init__(self, values):
        factories = {
            'ban_info': BanFactory(),
            'city': CityFactory(),
            'contacts': ContactListFactory(),
            'counters': CounterFactory(),
            'country': CountryFactory(),
            'cover': CoverFactory(),
            'crop_photo': CropPhotoFactory(),
            'links': LinkListFactory(),
            'market': MarketFactory(),
            'place': PlaceFactory()
        }
        super(Group, self).__init__(values, factories)
