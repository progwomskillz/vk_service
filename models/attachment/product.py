from .attachment import Attachment
from vk_service.factories.attachment import PriceFactory


class Product(Attachment):
    def __init__(self, values):
        factories = {
            'price': PriceFactory(),
        }
        super(Product, self).__init__(values, factories)
