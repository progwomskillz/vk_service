from vk_service.models.profile.photo import Photo


class PhotoFactory:
    def build(self, values):
        return Photo(values)
