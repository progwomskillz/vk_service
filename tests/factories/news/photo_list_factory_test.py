import unittest

from vk_service.factories.news.photo_list_factory import PhotoListFactory
from vk_service.models.news.photo import Photo
from vk_service.models.news.size import Size
from vk_service.models.news.like import Like
from vk_service.models.news.repost import Repost
from vk_service.models.news.comment import Comment


class PhotoListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = PhotoListFactory()
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
        self.values = [self.photo.copy(), self.photo.copy()]
        self.submodels = {
            'sizes': Size,
            'likes': Like,
            'reposts': Repost,
            'comments': Comment
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
                if isinstance(photo.__dict__[key], list):
                    for item in photo.__dict__[key]:
                        self.assertIsInstance(item, self.submodels[key])
                else:
                    self.assertIsInstance(photo.__dict__[key], self.submodels[key])
            self.assertEqual(photo.__dict__, values[i])


if __name__ == '__main__':
    unittest.main()
