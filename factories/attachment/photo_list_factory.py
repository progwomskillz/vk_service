from vk_service.models.attachment.photo import Photo


class PhotoListFactory:
    def build(self, values):
        return [Photo(value) for value in values]
