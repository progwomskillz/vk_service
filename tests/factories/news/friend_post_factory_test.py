import unittest

from vk_service.factories.news.friend_post_factory import FriendPostFactory
from vk_service.models.news.friend_post import FriendPost
from vk_service.models.news.friend_list_meta_data import FriendListMetaData
from vk_service.models.profile.profile import Profile
from vk_service.models.group.group import Group


class FriendPostFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = FriendPostFactory()
        self.friend = {'user_id': 53}
        self.friend_list = [self.friend.copy(), self.friend.copy()]
        self.friends = {'count': 2, 'items': self.friend_list.copy()}
        self.values = {
            'type': 'friend', 'source_id': 90330786, 'date': 1541696914,
            'friends': self.friends.copy()
        }
        self.submodels = {
            'friends': FriendListMetaData
        }
        self.profiles = [
            {
                'id': 90330786,
                'first_name': 'Михаил',
                'last_name': 'Давиденко',
                'sex': 2,
                'screen_name': 'id90330786',
                'photo_50': 'https://pp.userap...26rclnWFI.jpg?ava=1',
                'photo_100': 'https://pp.userap...tdmKR5BsA.jpg?ava=1',
                'online': 0
            }, {
                'id': 257473557,
                'first_name': 'Алина',
                'last_name': 'Ребро',
                'sex': 1,
                'screen_name': 'alina_efremova1',
                'photo_50': 'https://pp.userap...httPyCw6w.jpg?ava=1',
                'photo_100': 'https://pp.userap...f58bf8-vc.jpg?ava=1',
                'online': 0
            }
        ]
        self.groups = []

    def test_factory_build(self):
        values = self.values.copy()
        profiles = self.profiles.copy()
        groups = self.groups.copy()
        friend_post = self.factory.build(values, profiles, groups)
        self.assertIsInstance(friend_post, FriendPost)
        for key in self.submodels:
            values[key] = friend_post.__dict__[key]
        for key in self.submodels:
            self.assertIsInstance(friend_post.__dict__[key], self.submodels[key])
        if values['source_id'] > 0:
            self.assertIsInstance(friend_post.owner, Profile)
        else:
            self.assertIsInstance(friend_post.owner, Group)
        values['owner'] = friend_post.owner
        self.assertEqual(friend_post.__dict__, values)


if __name__ == '__main__':
    unittest.main()
