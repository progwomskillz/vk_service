import unittest

from vk_service.factories.news.like_factory import LikeFactory
from vk_service.models.news.like import Like


class LikeFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = LikeFactory()
        self.values = {'count': 2, 'user_likes': 0, 'can_like': 1, 'can_publish': 1}

    def test_factory_build(self):
        values = self.values.copy()
        comment = self.factory.build(values)
        self.assertIsInstance(comment, Comment)
        self.assertEqual(comment.__dict__, values)


if __name__ == '__main__':
    unittest.main()
