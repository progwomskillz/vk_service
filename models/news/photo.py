from vk_service.models.common.photo import Photo
from vk_service.factories.news.size_list_factory import SizeListFactory
from vk_service.factories.news.like_factory import LikeFactory
from vk_service.factories.news.repost_factory import RepostFactory
from vk_service.factories.news.comment_factory import CommentFactory


class Photo(Photo):
    def __init__(self, values):
        factories = {
            'sizes': SizeListFactory(),
            'likes': LikeFactory(),
            'reposts': RepostFactory(),
            'comments': CommentFactory()
        }
        super(Photo, self).__init__(values, factories)
