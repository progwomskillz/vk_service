from vk_service.models.attachment import Price


class PriceFactory:
    def build(self, values):
        return Price(values)
