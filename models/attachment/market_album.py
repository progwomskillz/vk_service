from .attachment import Attachment
from vk_service.factories.attachment import PhotoFactory


class MarketAlbum(Attachment):
    def __init__(self, values):
        factories = {
            'photo': PhotoFactory(),
        }
        super(MarketAlbum, self).__init__(values, factories)
