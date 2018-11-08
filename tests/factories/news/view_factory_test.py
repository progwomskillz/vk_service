import unittest

from vk_service.factories.news.view_factory import ViewFactory
from vk_service.models.news.view import View


class ViewFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = ViewFactory()
        self.values = {'count': 189}

    def test_factory_build(self):
        values = self.values.copy()
        view = self.factory.build(values)
        self.assertIsInstance(view, View)
        self.assertEqual(view.__dict__, values)


if __name__ == '__main__':
    unittest.main()
