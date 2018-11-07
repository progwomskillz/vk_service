import unittest

from vk_service.factories.group.market_factory import MarketFactory
from vk_service.models.group.market import Market
from vk_service.models.group.currency import Currency


class MarketFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = MarketFactory()
        self.currency = {'id': 1, 'name': 'RUB'}
        self.values = {
            'enabled': 1, 'price_min': 0, 'price_max': 99999,
            'main_album_id': 53, 'contact_id': 53,
            'currency': self.currency.copy(), 'currency_text': 'руб.'
        }
        self.submodels = {
            'currency': Currency
        }

    def test_factory_build(self):
        values = self.values.copy()
        market = self.factory.build(values)
        self.assertIsInstance(market, Market)
        for key in self.submodels:
            values[key] = market.__dict__[key]
        for key in self.submodels:
            self.assertIsInstance(market.__dict__[key], self.submodels[key])
        self.assertEqual(market.__dict__, values)


if __name__ == '__main__':
    unittest.main()
