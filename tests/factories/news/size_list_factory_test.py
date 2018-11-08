import unittest

from vk_service.factories.news.size_list_factory import SizeListFactory
from vk_service.models.news.size import Size


class SizeListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = SizeListFactory()
        self.size = {
            'src': 'http://example.com/m.jpg', 'width': 130, 'height': 87,
            'type': 'm'
        }
        self.values = [self.size.copy()]

    def test_factory_build(self):
        values = self.values.copy()
        sizes = self.factory.build(values)
        self.assertIsInstance(sizes, list)
        for i, size in enumerate(sizes):
            self.assertIsInstance(size, Size)
            self.assertEqual(size.__dict__, values[i])


if __name__ == '__main__':
    unittest.main()
