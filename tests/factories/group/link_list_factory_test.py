import unittest

from vk_service.factories.group.link_list_factory import LinkListFactory
from vk_service.models.group.link import Link


class LinkListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = LinkListFactory()
        self.link = {
            'id': 3, 'url': 'http://example.com/', 'name': 'Example',
            'desc': 'None', 'photo_50': 'http://example.com/50/',
            'photo_100': 'http://example.com/100/'
        }
        self.values = [self.link.copy(), self.link.copy(), self.link.copy()]

    def test_factory_build(self):
        values = self.values.copy()
        links = self.factory.build(values)
        self.assertIsInstance(links, list)
        for i, link in enumerate(links):
            self.assertIsInstance(link, Link)
            self.assertEqual(link.__dict__, values[i])


if __name__ == '__main__':
    unittest.main()
