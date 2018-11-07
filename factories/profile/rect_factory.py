from vk_service.models.profile.rect import Rect


class RectFactory:
    def build(self, values):
        return Rect(values)
