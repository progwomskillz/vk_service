from vk_service.models.attachment.like import Like


class LikeFactory:
    def build(self, values):
        return Like(values)
