import unittest

from vk_service.factories.group.currency_factory import CurrencyFactory
from vk_service.models.group.currency import Currency


class CurrencyFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = CurrencyFactory()
        self.values = {'id': 1, 'name': 'RUB'}

    def test_factory_build(self):
        values = self.values.copy()
        currency = self.factory.build(values)
        self.assertIsInstance(currency, Currency)
        self.assertEqual(currency.__dict__, values)


if __name__ == '__main__':
    unittest.main()
