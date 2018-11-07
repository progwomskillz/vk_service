from .attachment import Attachment
from vk_service.factories.attachment import ImageListFactory, ButtonFactory


class Card(Attachment):
    def __init__(self, values):
        factories = {
            'images': ImageListFactory(),
            'button': ButtonFactory()
        }
        super(Card, self).__init__(values, factories)
