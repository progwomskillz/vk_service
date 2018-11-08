import unittest

from vk_service.factories.news.comment_factory import CommentFactory
from vk_service.models.news.comment import Comment


class CommentFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = CommentFactory()
        self.values = {'count': 0, 'can_post': 1, 'groups_can_post': True}

    def test_factory_build(self):
        values = self.values.copy()
        comment = self.factory.build(values)
        self.assertIsInstance(comment, Comment)
        self.assertEqual(comment.__dict__, values)


if __name__ == '__main__':
    unittest.main()
