from vk_service.models.attachment.card import Card


class CardListFactory:
    def build(self, values):
        return [Card(value) for value in values]
