from vk_service.models.common.link import Link
from vk_service.factories.attachment.photo_factory import PhotoFactory
from vk_service.factories.attachment.product_factory import ProductFactory
from vk_service.factories.attachment.button_factory import ButtonFactory


class Link(Link):
    def __init__(self, values):
        factories = {
            'photo': PhotoFactory(),
            'product': ProductFactory(),
            'button': ButtonFactory(),
        }
        super(Link, self).__init__(values, factories)
