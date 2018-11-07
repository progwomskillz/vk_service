from vk_service.models.attachment import Photo


class PhotoListFactory:
    def build(self, values):
        return [Photo(value) for value in values]
