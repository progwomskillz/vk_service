from vk_service.models.news.friends import Friends


class FriendsFactory:
    def build(self, values):
        return Friends(values)
