from vk_service.models.news.repost import Repost


class RepostFactory:
    def build(self, values):
        return Repost(values)
