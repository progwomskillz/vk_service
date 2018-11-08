from .post import Post
from vk_service.factories.news.friends_factory import FriendsFactory


class FriendPost(Post):
    def __init__(self, post, profiles, groups):
        factories = {
            'friends': FriendsFactory()
        }
        super(FriendPost, self).__init__(post, profiles, groups, factories)
