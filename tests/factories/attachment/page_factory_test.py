import unittest

from vk_service.factories.attachment.page_factory import PageFactory
from vk_service.models.attachment.page import Page


class PageFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = PageFactory()
        self.values = {
            'id': 1, 'group_id': 23, 'creator_id': 53, 'title': 'Wiki',
            'current_user_can_edit': 1, 'current_user_can_edit_access': 1,
            'who_can_view': 1, 'who_can_edit': 0, 'edited': 65252522562,
            'created': 65252522562, 'editor_id': 53, 'views': 1154,
            'parent': 'Wiki parent1', 'parent2': 'Wiki parent2',
            'source': 'Text wiki page', 'html': '<p>Text wiki page</p>',
            'view_url': 'http://example.com/wiki/'
        }

    def test_factory_build(self):
        values = self.values.copy()
        page = self.factory.build(values)
        self.assertIsInstance(page, Page)
        self.assertEqual(page.__dict__, values)


if __name__ == '__main__':
    unittest.main()
