import unittest

from vk_service.factories.group.counter_factory import CounterFactory
from vk_service.models.group.counter import Counter


class CounterFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = CounterFactory()
        self.values = {
            'albums': 1, 'videos': 0, 'audios': 3, 'photos': 15, 'notes': 0
        }

    def test_factory_build(self):
        values = self.values.copy()
        counter = self.factory.build(values)
        self.assertIsInstance(counter, Counter)
        self.assertEqual(counter.__dict__, values)


if __name__ == '__main__':
    unittest.main()
