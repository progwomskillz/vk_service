from vk_service.models.attachment import Photo


class PhotoFactory:
    def build(self, values):
        return Photo(values)
