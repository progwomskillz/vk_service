from vk_service.models.attachment.price import Price


class PriceFactory:
    def build(self, values):
        return Price(values)
