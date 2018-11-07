from vk_service.models.attachment import AudioMessage


class AudioMessageFactory:
    def build(self, values):
        return AudioMessage(values)
