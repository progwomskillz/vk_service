import unittest

from vk_service.factories.news.wall_photo_post_factory import WallPhotoPostFactory
from vk_service.models.news.wall_photo_post import WallPhotoPost
from vk_service.models.news.photos import Photos
from vk_service.models.profile.profile import Profile
from vk_service.models.group.group import Group


class WallPhotoPostFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = WallPhotoPostFactory()
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
        self.photo_list = [self.photo.copy(), self.photo.copy()]
        self.photos = {'count': 2, 'items': self.photo_list.copy()}
        self.values = {
            "type": "wall_photo", "source_id": -41437811, "date": 1541681474,
            "post_id": 333960, 'photos': self.photos.copy()
        }
        self.submodels = {
            'photos': Photos
        }
        self.profiles = []
        self.groups = [
            {
                "id": 41437811, "name": "МХК",
                "screen_name": "mhkoff", "is_closed": 0,
                "type": "page", "is_admin": 0, "is_member": 1,
                "photo_50": "https://pp.userap...Gk3gGxO8c.jpg?ava=1",
                "photo_100": "https://pp.userap...jgK-93vSo.jpg?ava=1",
                "photo_200": "https://pp.userap...DjxFwb1A8.jpg?ava=1"
            }, {
                "id": 72495085, "name": "/dev/null",
                "screen_name": "tnull", "is_closed": 0,
                "type": "page", "is_admin": 0, "is_member": 1,
                "photo_50": "https://sun1-6.us...-h6o_8VS8.jpg?ava=1",
                "photo_100": "https://sun1-5.us...PTdjZrLgo.jpg?ava=1",
                "photo_200": "https://sun1-20.u...EBzYm5fAU.jpg?ava=1"
            }, {
                "id": 30666517, "name": "Типичный программист",
                "screen_name": "tproger", "is_closed": 0,
                "type": "page", "is_admin": 0, "is_member": 1,
                "photo_50": "https://pp.userap...KNrvjYkdo.jpg?ava=1",
                "photo_100": "https://pp.userap...JJG4iknq0.jpg?ava=1",
                "photo_200": "https://pp.userap...eV7nJitGY.jpg?ava=1"
            }
        ]

    def test_factory_build(self):
        values = self.values.copy()
        profiles = self.profiles.copy()
        groups = self.groups.copy()
        wall_photo_post = self.factory.build(values, profiles, groups)
        self.assertIsInstance(wall_photo_post, WallPhotoPost)
        for key in self.submodels:
            values[key] = wall_photo_post.__dict__[key]
        for key in self.submodels:
            self.assertIsInstance(wall_photo_post.__dict__[key], self.submodels[key])
        if values['source_id'] > 0:
            self.assertIsInstance(wall_photo_post.owner, Profile)
        else:
            self.assertIsInstance(wall_photo_post.owner, Group)
        values['owner'] = wall_photo_post.owner
        self.assertEqual(wall_photo_post.__dict__, values)


if __name__ == '__main__':
    unittest.main()
