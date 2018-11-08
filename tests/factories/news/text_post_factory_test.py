import unittest

from vk_service.factories.news.text_post_factory import TextPostFactory
from vk_service.models.news.text_post import TextPost
from vk_service.models.news.post_source import PostSource
from vk_service.models.news.comment import Comment
from vk_service.models.news.like import Like
from vk_service.models.news.repost import Repost
from vk_service.models.news.view import View


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

    def test_factory_build(self):
        values = self.values.copy()
        text_post = self.factory.build(values)
        self.assertIsInstance(text_post, TextPost)
        for key in self.submodels:
            values[key] = text_post.__dict__[key]
        for key in self.submodels:
            self.assertIsInstance(text_post.__dict__[key], self.submodels[key])
        self.assertEqual(text_post.__dict__, values)


if __name__ == '__main__':
    unittest.main()
