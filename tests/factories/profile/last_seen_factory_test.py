import unittest

from vk_service.factories.profile.last_seen_factory import LastSeenFactory
from vk_service.models.profile.last_seen import LastSeen


class LastSeenFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = LastSeenFactory()
        self.values = {'time': 51561265, 'platform': 1}

    def test_factory_build(self):
        values = self.values.copy()
        last_seen = self.factory.build(values)
        self.assertIsInstance(last_seen, LastSeen)
        self.assertEqual(last_seen.__dict__, values)


if __name__ == '__main__':
    unittest.main()
