import unittest

from vk_service.factories.attachment.like_factory import LikeFactory
from vk_service.models.attachment.like import Like


class LikeFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = LikeFactory()
        self.values = {
            'count': 23, 'user_likes': 1, 'can_like': 1, 'can_publish': 1
        }

    def test_factory_build(self):
        values = self.values.copy()
        like = self.factory.build(values)
        self.assertIsInstance(like, Like)
        self.assertEqual(like.__dict__, values)


if __name__ == '__main__':
    unittest.main()
