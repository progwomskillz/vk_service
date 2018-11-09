from .repost_source import RepostSource
from vk_service.factories.attachment.attachment_list_factory import AttachmentListFactory
from vk_service.factories.news.post_source_factory import PostSourceFactory


class RepostSourcePost(Post):
    def __init__(self, post, profiles, groups):
        factories = {
            'attachments': AttachmentListFactory(),
            'post_source': PostSourceFactory()
        }
        super(RepostSourcePost, self).__init__(post, profiles, groups, factories)
