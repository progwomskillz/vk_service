from vk_service.models.attachment.audio_message import AudioMessage


class AudioMessageFactory:
    def build(self, values):
        return AudioMessage(values)
