import unittest

from vk_service.factories.attachment.card_list_factory import CardListFactory
from vk_service.models.attachment.card import Card
from vk_service.models.attachment.image import Image
from vk_service.models.attachment.button import Button


class CardListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = CardListFactory()
        self.action = {'type': 'open_url', 'url': 'http://example.com/'}
        self.button = {'title': 'Button 1', 'action': self.action.copy()}
        self.image = {
            'url': 'http://example.com/im1/', 'width': 100, 'height': 50
        }
        self.images = [self.image.copy(), self.image.copy(), self.image.copy()]
        self.card = {
            'card_id': 1, 'link_url': 'http://example.com/card1/',
            'title': 'Card1', 'images': self.images.copy(),
            'button': self.button.copy(), 'price': '5487 RUB',
            'price_old': '6000 RUB'
        }
        self.values = [self.card.copy(), self.card.copy()]
        self.submodels = {
            'images': Image,
            'button': Button
        }

    def test_factory_build(self):
        values = self.values.copy()
        cards = self.factory.build(values)
        self.assertIsInstance(cards, list)
        for i, card in enumerate(cards):
            self.assertIsInstance(card, Card)
            for key in self.submodels:
                values[i][key] = card.__dict__[key]
            for key in self.submodels:
                value = self.submodels[key]
                if isinstance(card.__dict__[key], list):
                    for item in card.__dict__[key]:
                        self.assertIsInstance(item, value)
                else:
                    self.assertIsInstance(card.__dict__[key], value)
            self.assertEqual(card.__dict__, values[i])


if __name__ == '__main__':
    unittest.main()
