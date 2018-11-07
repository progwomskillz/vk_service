from vk_service.models.group.currency import Currency


class CurrencyFactory:
    def build(self, values):
        return Currency(values)
