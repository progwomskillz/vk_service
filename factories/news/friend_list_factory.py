from vk_service.models.news.friend import Friend


class FriendListFactory:
    def build(self, values):
        return [Friend(value) for value in values]
