from .attachment import Attachment
from vk_service.factories.attachment import (
    PhotoFactory, ProductFactory, ButtonFactory
)


class Link(Attachment):
    def __init__(self, values):
        factories = {
            'photo': PhotoFactory(),
            'product': ProductFactory(),
            'button': ButtonFactory(),
        }
        super(Link, self).__init__(values, factories)
