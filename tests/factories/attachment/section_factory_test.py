import unittest

from vk_service.factories.attachment.section_factory import SectionFactory
from vk_service.models.attachment.section import Section


class SectionFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = SectionFactory()
        self.values = {'id': 10, 'name': 'Section 10'}

    def test_factory_build(self):
        values = self.values.copy()
        section = self.factory.build(values)
        self.assertIsInstance(section, Section)
        self.assertEqual(section.__dict__, values)


if __name__ == '__main__':
    unittest.main()
