import unittest

from vk_service.factories.news.text_post_factory import TextPostFactory
from vk_service.models.news.text_post import TextPost
from vk_service.models.news.post_source import PostSource
from vk_service.models.news.comment import Comment
from vk_service.models.news.like import Like
from vk_service.models.news.repost import Repost
from vk_service.models.news.view import View
from vk_service.models.group.group import Group
from vk_service.models.profile.profile import Profile


class TextPostFactoryText(unittest.TestCase):
    def setUp(self):
        self.factory = TextPostFactory()
        self.size = {
            "type": "z",
            "url": "https://sun1-8.us...63b/K3VHq4yOQhQ.jpg",
            "width": 750, "height": 1080
        }
        self.sizes = [self.size.copy(), self.size.copy()]
        self.photo = {
            "id": 456303900, "album_id": -7,
            "owner_id": -41437811, "user_id": 100,
            "sizes": self.sizes.copy(), "text": "", "date": 1541681474, "post_id": 333960,
            "access_key": "b2db4cbd5df9a78a6e"
        }
        self.attachment = {
            "type": "photo", "photo": self.photo.copy()
        }
        self.attachments = [self.attachment.copy()]
        self.post_source = {"type": "vk"}
        self.comment = {
            "count": 34, "can_post": 1,
            "groups_can_post": True
        }
        self.like = {
            "count": 1380, "user_likes": 0,
            "can_like": 1, "can_publish": 1
        }
        self.repost = {"count": 24, "user_reposted": 0}
        self.view = {"count": 23098}
        self.values = {
            "type": "post", "source_id": -41437811, "date": 1541681474, "post_id": 333960,
            "post_type": "post", "text": "Хороший мальчик спас хороших мальчиков",
            "marked_as_ads": 0, "attachments": self.attachments.copy(),
            "post_source": self.post_source.copy(), "comments": self.comment.copy(),
            "likes": self.like.copy(), "reposts": self.repost.copy(),
            "views": self.view.copy()
        }
        self.submodels = {
            'attachments': list,
            'post_source': PostSource,
            'comments': Comment,
            'likes': Like,
            'reposts': Repost,
            'views': View
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
        text_post = self.factory.build(values, profiles, groups)
        self.assertIsInstance(text_post, TextPost)
        for key in self.submodels:
            values[key] = text_post.__dict__[key]
        for key in self.submodels:
            self.assertIsInstance(text_post.__dict__[key], self.submodels[key])
        if values['source_id'] > 0:
            self.assertIsInstance(text_post.owner, Profile)
        else:
            self.assertIsInstance(text_post.owner, Group)
        values['owner'] = text_post.owner
        self.assertEqual(text_post.__dict__, values)


if __name__ == '__main__':
    unittest.main()
