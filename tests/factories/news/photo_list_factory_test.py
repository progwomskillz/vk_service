import unittest

from vk_service.factories.news.photo_list_factory import PhotoListFactory
from vk_service.models.news.photo import Photo
from vk_service.models.news.size import Size


class PhotoListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = PhotoListFactory()
        self.size = {
            'src': 'http://example.com/m.jpg', 'width': 130,
            'height': 87, 'type': 'm'
        }
        self.sizes = [self.size.copy(), self.size.copy()]
        self.photo = {
            'id': 3, 'album_id': 2, 'owner_id': 53, 'user_id': 53, 'text': 'D',
            'date': 25748559, 'sizes': self.sizes.copy(), 'width': 153,
            'height': 154
        }
        self.values = [self.photo.copy(), self.photo.copy()]
        self.submodels = {
            'sizes': Size
        }

    def test_factory_build(self):
        values = self.values.copy()
        photos = self.factory.build(values)
        self.assertIsInstance(photos, list)
        for i, photo in enumerate(photos):
            self.assertIsInstance(photo, Photo)
            for key in self.submodels:
                values[i][key] = photo.__dict__[key]
            for key in self.submodels:
                for item in photo.__dict__[key]:
                    self.assertIsInstance(item, self.submodels[key])
            self.assertEqual(photo.__dict__, values[i])


if __name__ == '__main__':
    unittest.main()
