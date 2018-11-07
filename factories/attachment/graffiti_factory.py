from vk_service.models.attachment import Graffiti


class GraffitiFactory:
    def build(self, values):
        return Graffiti(values)
