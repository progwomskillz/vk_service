import unittest

from vk_service.factories.attachment.link_factory import LinkFactory
from vk_service.models.attachment.like import Link
from vk_service.models.attachment.photo import Photo
from vk_service.models.attachment.product import Product
from vk_service.models.attachment.button import Button


class LinkFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = LinkFactory()
        self.size = {
            'type': 'w', 'src': 'http://example.com/w/',
            'width': 130, 'height': 248,
        }
        self.sizes = [self.size.copy(), self.size.copy(), self.size.copy()]
        self.photo = {
            'id': 1, 'album_id': 58, 'owner_id': 53, 'user_id': 53,
            'text': 'No', 'date': 62224588, 'sizes': self.sizes.copy(),
            'width': 2580, 'height': 147
        }
        self.currency = {'id': 1, 'name': 'RUB'}
        self.price = {
            'amount': 487400, 'currency': self.currency.copy(),
            'text': '4874 руб.'
        }
        self.product = {'price': self.price.copy()}
        self.action = {'type': 'open_url', 'url': 'http://example.com/'}
        self.button = {'title': 'ClickMe', 'action': self.action.copy()}
        self.values = {
            'url': 'http://example.com/', 'title': 'Shop', 'caption': 'None',
            'description': 'Desc', 'photo': self.photo.copy(),
            'product': self.product.copy(), 'button': self.button.copy(),
            'preview_page': '959499_415640',
            'preview_url': 'http://example.com/'
        }
        self.submodels = {
            'photo': Photo,
            'product': Product,
            'button': Button
        }

    def test_factory_build(self):
        values = self.values.copy()
        link = self.factory.build(values)
        self.assertIsInstance(link, Link)
        for key in self.submodels:
            values[key] = link.__dict__[key]
        for key in self.submodels:
            self.assertIsInstance(link.__dict__[key], self.submodels[key])
        self.assertEqual(link.__dict__, values)


if __name__ == '__main__':
    unittest.main()
