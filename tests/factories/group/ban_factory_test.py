import unittest

from vk_service.factories.group.ban_factory import BanFactory
from vk_service.models.group.ban import Ban


class BanFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = BanFactory()
        self.values = {'end_date': 8411651, 'comment': 'None'}

    def test_factory_build(self):
        values = self.values.copy()
        ban = self.factory.build(values)
        self.assertIsInstance(ban, Ban)
        self.assertEqual(ban.__dict__, values)


if __name__ == '__main__':
    unittest.main()
