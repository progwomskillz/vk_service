from vk_service.models.common.video import Video
from vk_service.factories.news.like_factory import LikeFactory
from vk_service.factories.news.repost_factory import RepostFactory


class Video(Video):
    def __init__(self, values):
        factories = {
            'likes': LikeFactory(),
            'reposts': RepostFactory()
        }
        super(Video, self).__init__(values, factories)
