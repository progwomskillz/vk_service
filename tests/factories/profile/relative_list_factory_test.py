import unittest

from vk_service.factories.profile.relative_list_factory import RelativeListFactory
from vk_service.models.profile.relative import Relative


class RelativeListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = RelativeListFactory()
        self.relative = {'id': 5, 'name': 'Валентина', 'type': 'parent'}
        self.values = [self.relative.copy(), self.relative.copy()]

    def test_factory_build(self):
        values = self.values.copy()
        relatives = self.factory.build(values)
        self.assertIsInstance(relatives, list)
        for i, relative in enumerate(relatives):
            self.assertIsInstance(relative, Relative)
            self.assertEqual(relative.__dict__, values[i])


if __name__ == '__main__':
    unittest.main()
