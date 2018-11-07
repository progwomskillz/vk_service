from vk_service.models.attachment import Video


class VideoFactory:
    def build(self, values):
        return Video(values)
