from vk_service.models.news.like import Like


class LikeFactory:
    def build(self, values):
        return Like(values)
