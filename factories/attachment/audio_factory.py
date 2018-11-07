from vk_service.models.attachment import Audio


class AudioFactory:
    def build(self, values):
        return Audio(values)
