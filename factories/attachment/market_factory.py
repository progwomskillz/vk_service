from vk_service.models.attachment.market import Market


class MarketFactory:
    def build(self, values):
        return Market(values)
