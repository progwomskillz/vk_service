from .attachment import Attachment
from vk_service.factories.attachment import ImageListFactory


class Sticker(Attachment):
    def __init__(self, values):
        factories = {
            'images': ImageListFactory(),
            'images_with_background': ImageListFactory(),
        }
        super(Sticker, self).__init__(values, factories)
