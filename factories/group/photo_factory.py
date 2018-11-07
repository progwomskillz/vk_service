from vk_service.models.group.photo import Photo


class PhotoFactory:
    def build(self, values):
        return Photo(values)
