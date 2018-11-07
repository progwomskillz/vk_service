import unittest

from vk_service.factories.attachment.market_factory import MarketFactory
from vk_service.models.attachment.market import Market
from vk_service.models.attachment.price import Price
from vk_service.models.attachment.category import Category
from vk_service.models.attachment.photo import Photo
from vk_service.models.attachment.like import Like


class MarketFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = MarketFactory()
        self.currency = {'id': 1, 'name': 'RUB'}
        self.price = {
            'amount': 5155100, 'currency': self.currency.copy(),
            'text': '51551 руб.'
        }
        self.section = {'id': 1, 'name': 'My section'}
        self.category = {
            'id': 1, 'category': 'home', 'section': self.section.copy()
        }
        self.size = {
            'src': 'http://example.com/m.jpg', 'width': 130,
            'height': 87, 'type': 'm'
        }
        self.sizes = [self.size.copy(), self.size.copy(), self.size.copy()]
        self.photo = {
            'id': 3, 'album_id': 2, 'owner_id': 53, 'user_id': 53,
            'text': 'D', 'date': 25748559, 'sizes': self.sizes.copy(),
            'width': 153, 'height': 154
        }
        self.photos = [self.photo.copy(), self.photo.copy()]
        self.likes = {'user_likes': 1, 'count': 23}
        self.values = {
            'id': 2, 'owner_id': 53, 'title': 'Item1', 'description': 'None',
            'price': self.price.copy(), 'category': self.category.copy(),
            'thumb_photo': 'http://example.com/thumb/', 'date': 4145615,
            'availability': 0, 'photos': self.photos.copy(), 'can_comment': 1,
            'can_repost': 1, 'likes': self.likes.copy()
        }
        self.submodels = {
            'price': Price,
            'category': Category,
            'photos': Photo,
            'likes': Like
        }

    def test_factory_build(self):
        values = self.values.copy()
        market = self.factory.build(values)
        self.assertIsInstance(market, Market)
        for key in self.submodels:
            values[key] = market.__dict__[key]
        for key in self.submodels:
            value = self.submodels[key]
            if isinstance(market.__dict__[key], list):
                for item in market.__dict__[key]:
                    self.assertIsInstance(item, value)
            else:
                self.assertIsInstance(market.__dict__[key], value)
        self.assertEqual(market.__dict__, values)


if __name__ == '__main__':
    unittest.main()
