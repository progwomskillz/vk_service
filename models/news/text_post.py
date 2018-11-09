from .post import Post
from vk_service.factories.news.comment_factory import CommentFactory
from vk_service.factories.news.like_factory import LikeFactory
from vk_service.factories.news.repost_factory import RepostFactory
from vk_service.factories.attachment.attachment_list_factory import AttachmentListFactory
from vk_service.factories.news.geo_factory import GeoFactory
from vk_service.factories.news.view_factory import ViewFactory
from vk_service.factories.news.post_source_factory import PostSourceFactory
from vk_service.factories.news.repost_source_post_list_factory import RepostSourcePostListFactory


class TextPost(Post):
    def __init__(self, post, profiles, groups):
        factories = {
            'comments': CommentFactory(),
            'likes': LikeFactory(),
            'reposts': RepostFactory(),
            'attachments': AttachmentListFactory(),
            'geo': GeoFactory(),
            'views': ViewFactory(),
            'post_source': PostSourceFactory()
        }
        super(TextPost, self).__init__(post, profiles, groups, factories)
        if 'copy_history' in post:
            self.copy_history = self._set_copy_history(self.copy_history, profiles, groups)

    def _set_copy_history(self, copy_history, profiles, groups):
        factory = RepostSourcePostListFactory()
        return factory.build(copy_history, profiles, groups)
