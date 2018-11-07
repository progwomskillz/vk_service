import unittest

from vk_service.factories.attachment.product_factory import ProductFactory
from vk_service.models.attachment.product import Product
from vk_service.models.attachment.price import Price


class ProductFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = ProductFactory()
        self.currency = {'id': 1, 'name': 'RUB'}
        self.price = {
            'amount': 524100, 'currency': self.currency.copy(),
            'text': '5241 RUB'
        }
        self.values = {'price': self.price.copy()}
        self.submodels = {
            'price': Price
        }

    def test_factory_build(self):
        values = self.values.copy()
        product = self.factory.build(values)
        self.assertIsInstance(product, Product)
        for key in self.submodels:
            values[key] = product.__dict__[key]
        for key in self.submodels:
            self.assertIsInstance(product.__dict__[key], self.submodels[key])
        self.assertEqual(product.__dict__, values)


if __name__ == '__main__':
    unittest.main()
