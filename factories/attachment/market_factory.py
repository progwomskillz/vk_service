from vk_service.models.attachment import Market


class MarketFactory:
    def build(self, values):
        return Market(values)
