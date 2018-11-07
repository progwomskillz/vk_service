from vk_service.models.group.cover import Cover


class CoverFactory:
    def build(self, values):
        return Cover(values)
