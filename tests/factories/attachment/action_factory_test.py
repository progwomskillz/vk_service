import unittest

from vk_service.factories.attachment import ActionFactory
from vk_service.models.attachment import Action


class ActionFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = ActionFactory()
        self.values = {'type': 'open_url', 'url': 'http://example.com/'}

    def test_factory_build(self):
        values = self.values.copy()
        action = self.factory.build(values)
        self.assertIsInstance(action, Action)
        self.assertEqual(action.__dict__, values)


if __name__ == '__main__':
    unittest.main()
