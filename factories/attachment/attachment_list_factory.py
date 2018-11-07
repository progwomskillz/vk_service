from . import (
    PhotoFactory, VideoFactory, AudioFactory, DocFactory, LinkFactory,
    NoteFactory, PollFactory, PageFactory, AlbumFactory, MarketFactory,
    MarketAlbumFactory, StickerFactory, PrettyCardFactory
)


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
