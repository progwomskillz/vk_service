import unittest

from vk_service.factories.attachment.graffiti_factory import GraffitiFactory
from vk_service.models.attachment.graffiti import Graffiti


class GraffitiFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = GraffitiFactory()
        self.values = {
            'src': 'http://example.com/graffiti',
            'width': 588, 'height': 551
        }

    def test_factory_build(self):
        values = self.values.copy()
        graffiti = self.factory.build(values)
        self.assertIsInstance(graffiti, Graffiti)
        self.assertEqual(graffiti.__dict__, values)


if __name__ == '__main__':
    unittest.main()
