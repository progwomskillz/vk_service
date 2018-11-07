from .attachment import Attachment
from vk_service.factories.attachment import (
    PhotoFactory, GraffitiFactory, AudioMessageFactory
)


class Preview(Attachment):
    def __init__(self, values):
        factories = {
            'photo': PhotoFactory(),
            'graffiti': GraffitiFactory(),
            'audio_message': AudioMessageFactory()
        }
        super(Preview, self).__init__(values, factories)
