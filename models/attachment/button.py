from .attachment import Attachment
from vk_service.factories.attachment import ActionFactory


class Button(Attachment):
    def __init__(self, values):
        factories = {
            'action': ActionFactory()
        }
        super(Button, self).__init__(values, factories)
