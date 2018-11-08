import unittest

from vk_service.factories.news.photos_factory import PhotosFactory
from vk_service.models.news.photos import Photos
from vk_service.models.news.photo import Photo


class PhotosFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = PhotosFactory()
        self.size = {
            'src': 'http://example.com/m.jpg', 'width': 130, 'height': 87,
            'type': 'm'
        }
        self.sizes = [self.size.copy(), self.size.copy()]
        self.like = {'user_likes': 0, 'count': 5}
        self.repost = {'count': 5, 'user_reposted': 0}
        self.comment = {'count': 5}
        self.photo = {
            'id': 53, 'album_id': -7, 'owner_id': -31412, 'user_id': 100,
            'sizes': self.sizes.copy(), 'text': 'None', 'date': 52562326,
            'post_id': 515, 'access_key': '8541511asd', 'likes': self.like.copy(),
            'reposts': self.repost.copy(), 'comments': self.comment.copy(),
            'can_comment': 1, 'can_repost': 1
        }
        self.photos = [self.photo.copy(), self.photo.copy()]
        self.values = {'count': 2, 'items': self.photos.copy()}
        self.submodels = {
            'items': Photo
        }

    def test_factory_build(self):
        values = self.values.copy()
        photos = self.factory.build(values)
        for key in self.submodels:
            values[key] = photos.__dict__[key]
        for key in self.submodels:
            for item in photos.__dict__[key]:
                self.assertIsInstance(item, self.submodels[key])
        self.assertIsInstance(photos, Photos)
        self.assertEqual(photos.__dict__, values)


if __name__ == '__main__':
    unittest.main()
