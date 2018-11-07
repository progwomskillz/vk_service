import unittest

from vk_service.factories.attachment.price_factory import PriceFactory
from vk_service.models.attachment.price import Price
from vk_service.models.attachment.currency import Currency


class PriceFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = PriceFactory()
        self.currency = {'id': 1, 'name': 'RUB'}
        self.values = {
            'amount': 524100, 'currency': self.currency.copy(),
            'text': '5241 RUB'
        }
        self.submodels = {
            'currency': Currency
        }

    def test_factory_build(self):
        values = self.values.copy()
        price = self.factory.build(values)
        self.assertIsInstance(price, Price)
        for key in self.submodels:
            values[key] = price.__dict__[key]
        for key in self.submodels:
            self.assertIsInstance(price.__dict__[key], self.submodels[key])
        self.assertEqual(price.__dict__, values)


if __name__ == '__main__':
    unittest.main()
