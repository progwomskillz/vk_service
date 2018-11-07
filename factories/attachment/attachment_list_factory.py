from .photo_factory import PhotoFactory
from .video_factory import VideoFactory
from .audio_factory import AudioFactory
from .doc_factory import DocFactory
from .link_factory import LinkFactory
from .note_factory import NoteFactory
from .poll_factory import PollFactory
from .page_factory import PageFactory
from .album_factory import AlbumFactory
from .market_factory import MarketFactory
from .market_album_factory import MarketAlbumFactory
from .sticker_factory import StickerFactory
from .pretty_card_factory import PrettyCardFactory


class AttachmentListFactory:
    def build(self, values):
        factories = {
            'photo': PhotoFactory(),
            'video': VideoFactory(),
            'audio': AudioFactory(),
            'doc': DocFactory(),
            'link': LinkFactory(),
            'note': NoteFactory(),
            'poll': PollFactory(),
            'page': PageFactory(),
            'album': AlbumFactory(),
            'market': MarketFactory(),
            'market_album': MarketAlbumFactory(),
            'sticker': StickerFactory(),
            'pretty_cards': PrettyCardFactory(),
        }

        attachments = []
        for value in values:
            factory = factories[value['type']]
            attachment = factory.build(value[value['type']])
            attachments.append(attachment)
        return attachments
