from vk_service.models.attachment.currency import Currency


class CurrencyFactory:
    def build(self, values):
        return Currency(values)
