from .attachment import Attachment
from vk_service.factories.attachment.photo_factory import PhotoFactory


class Album(Attachment):
    def __init__(self, values):
        factories = {
            'thumb': PhotoFactory(),
        }
        super(Album, self).__init__(values, factories)
