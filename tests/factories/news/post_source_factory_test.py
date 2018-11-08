import unittest

from vk_service.factories.news.post_source_factory import PostSourceFactory
from vk_service.models.news.post_source import PostSource


class PostSourceFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = PostSourceFactory()
        self.values = {'type': 'vk'}

    def test_factory_build(self):
        values = self.values.copy()
        post_source = self.factory.build(values)
        self.assertIsInstance(post_source, PostSource)
        self.assertEqual(post_source.__dict__, values)


if __name__ == '__main__':
    unittest.main()
