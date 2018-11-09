from vk_service.models.news.video import Video


class VideoListFactory:
    def build(self, values):
        return [Video(value) for value in values]
