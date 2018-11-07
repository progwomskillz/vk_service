from vk_service.models.attachment import Like


class LikeFactory:
    def build(self, values):
        return Like(values)
