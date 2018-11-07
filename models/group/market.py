from vk_service.models.common.market import Market
from vk_service.factories.group.currency_factory import CurrencyFactory


class Market(Market):
    def __init__(self, values):
        factories = {
            'currency': CurrencyFactory()
        }
        super(Market, self).__init__(values, factories)
