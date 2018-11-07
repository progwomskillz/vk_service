from vk_service.models.attachment.graffiti import Graffiti


class GraffitiFactory:
    def build(self, values):
        return Graffiti(values)
