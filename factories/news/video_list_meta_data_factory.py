from vk_service.models.news.video_list_meta_data import VideoListMetaData


class VideoListMetaDataFactory:
    def build(self, values):
        return VideoListMetaData(values)
