from vk_service.models.attachment.video import Video


class VideoFactory:
    def build(self, values):
        return Video(values)
