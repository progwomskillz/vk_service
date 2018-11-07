from vk_service.models.profile.relative import Relative


class RelativeListFactory:
    def build(self, values):
        return [Relative(value) for value in values]
