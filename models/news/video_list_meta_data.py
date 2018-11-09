from vk_service.models.common.common import Common
from vk_service.factories.news.video_list_factory import VideoListFactory


class VideoListMetaData(Common):
    def __init__(self, values):
        factories = {
            'items': VideoListFactory()
        }
        super(VideoListMetaData, self).__init__(values, factories)
