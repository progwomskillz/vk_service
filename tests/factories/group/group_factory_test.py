import unittest

from vk_service.factories.group.group_factory import GroupFactory
from vk_service.models.group.group import Group
from vk_service.models.group.ban import Ban
from vk_service.models.group.city import City
from vk_service.models.group.contact import Contact
from vk_service.models.group.counter import Counter
from vk_service.models.group.country import Country
from vk_service.models.group.cover import Cover
from vk_service.models.group.crop_photo import CropPhoto
from vk_service.models.group.link import Link
from vk_service.models.group.market import Market
from vk_service.models.group.place import Place


class GroupFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = GroupFactory()
        self.ban = {'end_date': 8411651, 'comment': 'None'}
        self.city = {'id': 1, 'title': 'Moscow'}
        self.contact = {
            'user_id': 53, 'desc': 'Editor', 'phone': '000',
            'email': 'Editor@example.com'
        }
        self.contacts = [self.contact.copy(), self.contact.copy()]
        self.counter = {
            'albums': 1, 'videos': 0, 'audios': 3, 'photos': 15, 'notes': 0
        }
        self.country = {'id': 1, 'title': 'Russia'}
        self.image = {
            'src': 'http://example.com/m.jpg', 'width': 130, 'height': 87,
            'type': 'm'
        }
        self.images = [self.image.copy(), self.image.copy(), self.image.copy()]
        self.cover = {'enabled': 1, 'images': self.images.copy()}
        self.photo = {'id': 5}
        self.crop = {'x': 1, 'y': 1, 'x2': 99, 'y2': 99}
        self.rect = {'x': 1, 'y': 1, 'x2': 99, 'y2': 99}
        self.crop_photo = {
            'photo': self.photo.copy(),
            'crop': self.crop.copy(),
            'rect': self.rect.copy()
        }
        self.link = {
            'id': 3, 'url': 'http://example.com/', 'name': 'Example',
            'desc': 'None', 'photo_50': 'http://example.com/50/',
            'photo_100': 'http://example.com/100/'
        }
        self.links = [self.link.copy(), self.link.copy(), self.link.copy()]
        self.currency = {'id': 1, 'name': 'RUB'}
        self.market = {
            'enabled': 1, 'price_min': 0, 'price_max': 99999,
            'main_album_id': 53, 'contact_id': 53,
            'currency': self.currency.copy(), 'currency_text': 'руб.'
        }
        self.place = {
            'id': 1, 'title': 'RedS', 'latitude': 87, 'longitude': 178,
            'type': 'Park', 'country': 1, 'city': 1, 'address': 'RS st. 1'
        }
        self.values = {
            'id': 91838942, 'name': 'Example', 'screen_name': 'id91838942',
            'is_closed': 0, 'type': 'page', 'is_admin': 0, 'is_member': 1,
            'photo_50': 'https://pp.userap...K8twDQunk.jpg?ava=1',
            'photo_100': 'https://pp.userap...K8twDQunk.jpg?ava=1',
            'photo_200': 'https://pp.userap...K8twDQunk.jpg?ava=1',
            'ban_info': self.ban.copy(),
            'city': self.city.copy(),
            'contacts': self.contacts.copy(),
            'counters': self.counter.copy(),
            'country': self.country.copy(),
            'cover': self.cover.copy(),
            'crop_photo': self.crop_photo.copy(),
            'links': self.links.copy(),
            'market': self.market.copy(),
            'place': self.place.copy()
        }
        self.submodels = {
            'ban_info': Ban,
            'city': City,
            'contacts': Contact,
            'counters': Counter,
            'country': Country,
            'cover': Cover,
            'crop_photo': CropPhoto,
            'links': Link,
            'market': Market,
            'place': Place
        }

    def test_factory_build(self):
        values = self.values.copy()
        group = self.factory.build(values)
        self.assertIsInstance(group, Group)
        for key in self.submodels:
            values[key] = group.__dict__[key]
        for key in self.submodels:
            value = self.submodels[key]
            if isinstance(group.__dict__[key], list):
                for item in group.__dict__[key]:
                    self.assertIsInstance(item, value)
            else:
                self.assertIsInstance(group.__dict__[key], value)
        self.assertEqual(group.__dict__, values)


if __name__ == '__main__':
    unittest.main()
