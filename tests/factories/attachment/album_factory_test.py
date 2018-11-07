import unittest

from vk_service.factories.attachment.album_factory import AlbumFactory
from vk_service.models.attachment.album import Album
from vk_service.models.attachment.photo import Photo


class AlbumFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = AlbumFactory()
        self.size = {
            'src': 'http://example.com/m.jpg', 'width': 130,
            'height': 87, 'type': 'm'
        }
        self.sizes = [self.size.copy(), self.size.copy(), self.size.copy()]
        self.thumb = {
            'id': 3, 'album_id': 2, 'owner_id': 53, 'user_id': 53,
            'text': 'D', 'date': 25748559, 'sizes': self.sizes.copy(),
            'width': 153, 'height': 154
        }
        self.values = {
            'id': 2, 'thumb': self.thumb.copy(), 'owner_id': 53,
            'title': 'MyAlbum', 'description': 'None',
            'created': 25748569, 'updated': 25748579, 'size': 3
        }
        self.submodels = {
            'thumb': Photo
        }

    def test_factory_build(self):
        values = self.values.copy()
        album = self.factory.build(values)
        self.assertIsInstance(album, Album)
        for key in self.submodels:
            values[key] = album.__dict__[key]
        for key in self.submodels:
            self.assertIsInstance(album.__dict__[key], self.submodels[key])
        self.assertEqual(album.__dict__, values)


if __name__ == '__main__':
    unittest.main()
