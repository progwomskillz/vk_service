import unittest

from vk_service.factories.attachment.market_album_factory import MarketAlbumFactory
from vk_service.models.attachment.market_album import MarketAlbum
from vk_service.models.attachment.photo import Photo


class MarketAlbumFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = MarketAlbumFactory()
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
        self.values = {
            'id': 2, 'owner_id': 53, 'title': 'Shopping',
            'photo': self.photo.copy(), 'count': 5, 'updated_time': 55455541
        }
        self.submodels = {
            'photo': Photo
        }

    def test_factory_build(self):
        values = self.values.copy()
        market_album = self.factory.build(values)
        self.assertIsInstance(market_album, MarketAlbum)
        for key in self.submodels:
            values[key] = market_album.__dict__[key]
        for key in self.submodels:
            value = self.submodels[key]
            self.assertIsInstance(market_album.__dict__[key], value)
        self.assertEqual(market_album.__dict__, values)


if __name__ == '__main__':
    unittest.main()
