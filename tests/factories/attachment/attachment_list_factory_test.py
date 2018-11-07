import unittest

from vk_service.factories.attachment import AttachmentListFactory
from vk_service.models.attachment import (
    Photo, Video, Audio, Doc, Link, Note, Poll, Page, Album, Market,
    MarketAlbum, Sticker, PrettyCard
)


class AttachmentListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = AttachmentListFactory()
        self.values = [
            {'type': 'photo', 'photo': {}},
            {'type': 'video', 'video': {}},
            {'type': 'audio', 'audio': {}},
            {'type': 'doc', 'doc': {}},
            {'type': 'link', 'link': {}},
            {'type': 'note', 'note': {}},
            {'type': 'poll', 'poll': {}},
            {'type': 'page', 'page': {}},
            {'type': 'album', 'album': {}},
            {'type': 'market', 'market': {}},
            {'type': 'market_album', 'market_album': {}},
            {'type': 'sticker', 'sticker': {}},
            {'type': 'pretty_cards', 'pretty_cards': {}}
        ]
        self.submodels = {
            'photo': Photo, 'video': Video, 'audio': Audio, 'doc': Doc,
            'link': Link, 'note': Note, 'poll': Poll, 'page': Page,
            'album': Album, 'market': Market, 'market_album': MarketAlbum,
            'sticker': Sticker, 'pretty_cards': PrettyCard
        }

    def test_factory_build(self):
        values = self.values.copy()
        attachments = self.factory.build(values)
        self.assertIsInstance(attachments, list)
        for i, attachment in enumerate(attachments):
            type_str = values[i]['type']
            self.assertIsInstance(attachment, self.submodels[type_str])
            self.assertEqual(attachment.__dict__, self.values[i][type_str])


if __name__ == '__main__':
    unittest.main()
