import unittest

from vk_service.factories.news.repost_factory import RepostFactory
from vk_service.models.news.repost import Repost


class RepostFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = RepostFactory()
        self.values = {'count': 0, 'user_reposted': 0}

    def test_factory_build(self):
        values = self.values.copy()
        repost = self.factory.build(values)
        self.assertIsInstance(repost, Repost)
        self.assertEqual(repost.__dict__, values)


if __name__ == '__main__':
    unittest.main()
