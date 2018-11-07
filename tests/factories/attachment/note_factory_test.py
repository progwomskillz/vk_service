import unittest

from vk_service.factories.attachment.note_factory import NoteFactory
from vk_service.models.attachment.note import Note


class NoteFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = NoteFactory()
        self.values = {
            'id': 1, 'owner_id': 53, 'title': 'Note1', 'text': 'text1',
            'date': 855251, 'comments': 52, 'read_comments': 50,
            'view_url': 'http://example.com/note1'
        }

    def test_factory_build(self):
        values = self.values.copy()
        note = self.factory.build(values)
        self.assertIsInstance(note, Note)
        self.assertEqual(note.__dict__, values)


if __name__ == '__main__':
    unittest.main()
