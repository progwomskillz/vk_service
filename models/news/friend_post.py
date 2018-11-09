from .post import Post
from vk_service.factories.news.friend_list_meta_data_factory import FriendListMetaDataFactory


class FriendPost(Post):
    def __init__(self, post, profiles, groups):
        factories = {
            'friends': FriendListMetaDataFactory()
        }
        super(FriendPost, self).__init__(post, profiles, groups, factories)
