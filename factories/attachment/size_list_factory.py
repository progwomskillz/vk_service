from vk_service.models.attachment import Size


class SizeListFactory:
    def build(self, values):
        return [Size(value) for value in values]
