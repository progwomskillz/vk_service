from vk_service.models.group.market import Market


class MarketFactory:
    def build(self, values):
        return Market(values)
