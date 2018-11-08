
from vk_service.models.news.friend_post import FriendPost


class FriendPostFactory:
    def build(self, post, profiles, groups):
        return FriendPost(post, profiles, groups)
