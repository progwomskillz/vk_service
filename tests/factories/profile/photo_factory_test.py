import unittest

from vk_service.factories.profile.photo_factory import PhotoFactory
from vk_service.models.profile.photo import Photo
from vk_service.models.profile.size import Size


class PhotoFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = PhotoFactory()
        self.size = {
            'src': 'http://example.com/m.jpg', 'width': 130,
            'height': 87, 'type': 'm'
        }
        self.sizes = [self.size.copy(), self.size.copy()]
        self.values = {
            'id': 3, 'album_id': 2, 'owner_id': 53, 'user_id': 53, 'text': 'D',
            'date': 25748559, 'sizes': self.sizes.copy(), 'width': 153,
            'height': 154
        }
        self.submodels = {
            'sizes': Size
        }

    def test_factory_build(self):
        values = self.values.copy()
        photo = self.factory.build(values)
        self.assertIsInstance(photo, Photo)
        for key in self.submodels:
            values[key] = photo.__dict__[key]
        for key in self.submodels:
            for item in photo.__dict__[key]:
                self.assertIsInstance(item, self.submodels[key])
        self.assertEqual(photo.__dict__, values)


if __name__ == '__main__':
    unittest.main()
