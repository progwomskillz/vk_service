from .post import Post
from vk_service.factories.news.video_list_meta_data_factory import VideoListMetaDataFactory


class VideoPost(Post):
    def __init__(self, post, profiles, groups):
        factories = {
            'video': VideoListMetaDataFactory()
        }
        super(VideoPost, self).__init__(post, profiles, groups, factories)
