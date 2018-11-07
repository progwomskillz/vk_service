from vk_service.models.attachment import Currency


class CurrencyFactory:
    def build(self, values):
        return Currency(values)
