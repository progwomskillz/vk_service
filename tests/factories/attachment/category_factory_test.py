import unittest

from vk_service.factories.attachment.category_factory import CategoryFactory
from vk_service.models.attachment.category import Category
from vk_service.models.attachment.section import Section


class CategoryFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = CategoryFactory()
        self.section = {'id': 2, 'name': 'SectionOne'}
        self.values = {
            'id': 2, 'name': 'MyCategory', 'section': self.section.copy()
        }
        self.submodels = {
            'section': Section
        }

    def test_factory_build(self):
        values = self.values.copy()
        category = self.factory.build(values)
        self.assertIsInstance(category, Category)
        for key in self.submodels:
            values[key] = category.__dict__[key]
        for key in self.submodels:
            self.assertIsInstance(category.__dict__[key], self.submodels[key])
        self.assertEqual(category.__dict__, values)


if __name__ == '__main__':
    unittest.main()
