from vk_service.models.attachment import PrettyCard


class PrettyCardFactory:
    def build(self, values):
        return PrettyCard(values)
