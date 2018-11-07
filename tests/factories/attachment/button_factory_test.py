import unittest

from vk_service.factories.attachment.button_factory import ButtonFactory
from vk_service.models.attachment.button import Button
from vk_service.models.attachment.action import Action


class ButtonFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = ButtonFactory()
        self.action = {'type': 'open_url', 'url': 'http://example.com/'}
        self.values = {'title': 'Button 1', 'action': self.action.copy()}
        self.submodels = {
            'action': Action
        }

    def test_factory_build(self):
        values = self.values.copy()
        button = self.factory.build(values)
        self.assertIsInstance(button, Button)
        for key in self.submodels:
            values[key] = button.__dict__[key]
        for key in self.submodels:
            self.assertIsInstance(button.__dict__[key], self.submodels[key])
        self.assertEqual(button.__dict__, values)


if __name__ == '__main__':
    unittest.main()
