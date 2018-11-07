from vk_service.models.attachment import Image


class ImageListFactory:
    def build(self, values):
        return [Image(value) for value in values]
