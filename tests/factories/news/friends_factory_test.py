import unittest

from vk_service.factories.news.friends_factory import FriendsFactory
from vk_service.models.news.friends import Friends
from vk_service.models.news.friend import Friend


class FriendsFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = FriendsFactory()
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
        self.assertIsInstance(friends, Friends)
        self.assertEqual(friends.__dict__, values)


if __name__ == '__main__':
    unittest.main()
