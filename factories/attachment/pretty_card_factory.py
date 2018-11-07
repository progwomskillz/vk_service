from vk_service.models.attachment.pretty_card import PrettyCard


class PrettyCardFactory:
    def build(self, values):
        return PrettyCard(values)
