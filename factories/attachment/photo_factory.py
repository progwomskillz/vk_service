from vk_service.models.attachment.photo import Photo


class PhotoFactory:
    def build(self, values):
        return Photo(values)
