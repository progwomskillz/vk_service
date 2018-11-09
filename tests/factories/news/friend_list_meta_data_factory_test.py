import unittest

from vk_service.factories.news.friend_list_meta_data_factory import FriendListMetaDataFactory
from vk_service.models.news.friend_list_meta_data import FriendListMetaData
from vk_service.models.news.friend import Friend


class FriendListMetaDataFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = FriendListMetaDataFactory()
        self.friend = {'user_id': 53}
        self.friends = [self.friend.copy(), self.friend.copy()]
        self.values = {'count': 2, 'items': self.friends.copy()}
        self.submodels = {
            'items': Friend
        }

    def test_factory_build(self):
        values = self.values.copy()
        friends = self.factory.build(values)
        for key in self.submodels:
            values[key] = friends.__dict__[key]
        for key in self.submodels:
            for item in friends.__dict__[key]:
                self.assertIsInstance(item, self.submodels[key])
        self.assertIsInstance(friends, FriendListMetaData)
        self.assertEqual(friends.__dict__, values)


if __name__ == '__main__':
    unittest.main()
