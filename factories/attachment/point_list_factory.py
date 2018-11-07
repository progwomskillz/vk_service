from vk_service.models.attachment import Point


class PointListFactory:
    def build(self, values):
        return [Point(value) for value in values]
