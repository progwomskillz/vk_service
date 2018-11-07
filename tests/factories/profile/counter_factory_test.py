import unittest

from vk_service.factories.profile.counter_factory import CounterFactory
from vk_service.models.profile.counter import Counter


class CounterFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = CounterFactory()
        self.values = {
            'albums': 1, 'videos': 0, 'audios': 3, 'photos': 15, 'notes': 0,
            'friends': 152, 'groups': 1474, 'online_friends': 5,
            'mutual_friends': 1, 'user_videos': 0, 'followers': 251,
            'pages': 54
        }

    def test_factory_build(self):
        values = self.values.copy()
        counter = self.factory.build(values)
        self.assertIsInstance(counter, Counter)
        self.assertEqual(counter.__dict__, values)


if __name__ == '__main__':
    unittest.main()
