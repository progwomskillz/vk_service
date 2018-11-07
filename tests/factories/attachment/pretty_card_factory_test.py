import unittest

from vk_service.factories.attachment.pretty_card_factory import PrettyCardFactory
from vk_service.models.attachment.pretty_card import PrettyCard
from vk_service.models.attachment.card import Card


class PrettyCardFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = PrettyCardFactory()
        self.image = {
            'url': 'http://example.com/im1/', 'width': 100,
            'height': 50
        }
        self.images = [self.image.copy(), self.image.copy()]
        self.action = {'type': 'open_url', 'url': 'http://example.com/'}
        self.button = {'title': 'Button 1', 'action': self.action.copy()}
        self.card = {
            'card_id': 1, 'link_url': 'http://example.com/card1/',
            'title': 'Card1', 'images': self.images.copy(),
            'button': self.button.copy(), 'price': '5487 RUB',
            'price_old': '6000 RUB'
        }
        self.cards = [self.card.copy(), self.card.copy()]
        self.values = {'cards': self.cards.copy()}
        self.submodels = {
            'cards': Card
        }

    def test_factory_build(self):
        values = self.values.copy()
        pretty_card = self.factory.build(values)
        self.assertIsInstance(pretty_card, PrettyCard)
        for key in self.submodels:
            values[key] = pretty_card.__dict__[key]
        for key in self.submodels:
            for item in pretty_card.__dict__[key]:
                self.assertIsInstance(item, self.submodels[key])
        self.assertEqual(pretty_card.__dict__, values)


if __name__ == '__main__':
    unittest.main()
