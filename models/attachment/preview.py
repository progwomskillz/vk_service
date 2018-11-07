from .attachment import Attachment
from vk_service.factories.attachment.photo_factory import PhotoFactory
from vk_service.factories.attachment.graffiti_factory import GraffitiFactory
from vk_service.factories.attachment.audio_message_factory import AudioMessageFactory


class Preview(Attachment):
    def __init__(self, values):
        factories = {
            'photo': PhotoFactory(),
            'graffiti': GraffitiFactory(),
            'audio_message': AudioMessageFactory()
        }
        super(Preview, self).__init__(values, factories)
