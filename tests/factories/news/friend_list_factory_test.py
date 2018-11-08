import unittest

from vk_service.factories.news.friend_list_factory import FriendListFactory
from vk_service.models.news.friend import Friend


class FriendListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = FriendListFactory()
        self.friend = {'user_id': 53}
        self.values = [self.friend.copy(), self.friend.copy()]

    def test_factory_build(self):
        values = self.values.copy()
        friends = self.factory.build(values)
        self.assertIsInstance(friends, list)
        for i, friend in enumerate(friends):
            self.assertIsInstance(friend, Friend)
            print(friend.__dict__)
            print(values[i])
            self.assertEqual(friend.__dict__, values[i])


if __name__ == '__main__':
    unittest.main()
