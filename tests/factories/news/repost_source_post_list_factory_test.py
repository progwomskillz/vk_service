import unittest

from vk_service.factories.news.repost_source_post_list_factory import RepostSourcePostListFactory
from vk_service.models.news.repost_source_post import RepostSourcePost
from vk_service.models.news.post_source import PostSource
from vk_service.models.profile.profile import Profile
from vk_service.models.group.group import Group


class RepostSourcePostListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = RepostSourcePostListFactory()
        self.post_source = {'type': 'vk'}
        self.repost = {
            'id': 456249429, 'owner_id': -33016113, 'from_id': -33016113,
            'date': 1539987637, 'post_type': 'photo', 'text': '',
            'attachments': [], 'post_source': self.post_source.copy()
        }
        self.values =[self.repost.copy(), self.repost.copy()]
        self.submodels = {
            'attachments': list,
            'post_source': PostSource
        }
        self.profiles = []
        self.groups = [
            {
                'id': 33016113, 'name': 'МХК',
                'screen_name': 'mhkoff', 'is_closed': 0,
                'type': 'page', 'is_admin': 0, 'is_member': 1,
                'photo_50': 'https://pp.userap...Gk3gGxO8c.jpg?ava=1',
                'photo_100': 'https://pp.userap...jgK-93vSo.jpg?ava=1',
                'photo_200': 'https://pp.userap...DjxFwb1A8.jpg?ava=1'
            }, {
                'id': 72495085, 'name': '/dev/null',
                'screen_name': 'tnull', 'is_closed': 0,
                'type': 'page', 'is_admin': 0, 'is_member': 1,
                'photo_50': 'https://sun1-6.us...-h6o_8VS8.jpg?ava=1',
                'photo_100': 'https://sun1-5.us...PTdjZrLgo.jpg?ava=1',
                'photo_200': 'https://sun1-20.u...EBzYm5fAU.jpg?ava=1'
            }, {
                'id': 30666517, 'name': 'Типичный программист',
                'screen_name': 'tproger', 'is_closed': 0,
                'type': 'page', 'is_admin': 0, 'is_member': 1,
                'photo_50': 'https://pp.userap...KNrvjYkdo.jpg?ava=1',
                'photo_100': 'https://pp.userap...JJG4iknq0.jpg?ava=1',
                'photo_200': 'https://pp.userap...eV7nJitGY.jpg?ava=1'
            }
        ]

    def test_factory_build(self):
        values = self.values.copy()
        profiles = self.profiles.copy()
        groups = self.groups.copy()
        repost_source_posts = self.factory.build(values, profiles, groups)
        self.assertIsInstance(repost_source_posts, list)
        for i, repost_source_post  in enumerate(repost_source_posts):
            self.assertIsInstance(repost_source_post, RepostSourcePost)
            for key in self.submodels:
                values[i][key] = repost_source_post.__dict__[key]
            for key in self.submodels:
                self.assertIsInstance(repost_source_post.__dict__[key], self.submodels[key])
            if values[i]['owner_id'] > 0:
                self.assertIsInstance(repost_source_post.owner, Profile)
            else:
                self.assertIsInstance(repost_source_post.owner, Group)
            values[i]['owner'] = repost_source_post.owner
            self.assertEqual(repost_source_post.__dict__, values[i])


if __name__ == '__main__':
    unittest.main()
