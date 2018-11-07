from .attachment import Attachment
from vk_service.factories.attachment.image_list_factory import ImageListFactory
from vk_service.factories.attachment.button_factory import ButtonFactory


class Card(Attachment):
    def __init__(self, values):
        factories = {
            'images': ImageListFactory(),
            'button': ButtonFactory()
        }
        super(Card, self).__init__(values, factories)
