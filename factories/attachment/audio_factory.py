from vk_service.models.attachment.audio import Audio


class AudioFactory:
    def build(self, values):
        return Audio(values)
