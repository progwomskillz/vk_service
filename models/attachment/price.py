from .attachment import Attachment
from vk_service.factories.attachment.currency_factory import CurrencyFactory


class Price(Attachment):
    def __init__(self, values):
        factories = {
            'currency': CurrencyFactory(),
        }
        super(Price, self).__init__(values, factories)
