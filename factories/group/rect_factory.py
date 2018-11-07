from vk_service.models.group.rect import Rect


class RectFactory:
    def build(self, values):
        return Rect(values)
