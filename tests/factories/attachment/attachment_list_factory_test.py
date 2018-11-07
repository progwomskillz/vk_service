import unittest

from vk_service.factories.attachment.attachment_list_factory import AttachmentListFactory
from vk_service.models.attachment.photo import Photo
from vk_service.models.attachment.video import Video
from vk_service.models.attachment.audio import Audio
from vk_service.models.attachment.doc import Doc
from vk_service.models.attachment.link import Link
from vk_service.models.attachment.note import Note
from vk_service.models.attachment.poll import Poll
from vk_service.models.attachment.page import Page
from vk_service.models.attachment.album import Album
from vk_service.models.attachment.market import Market
from vk_service.models.attachment.market_album import MarketAlbum
from vk_service.models.attachment.sticker import Sticker
from vk_service.models.attachment.pretty_card import PrettyCard


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
