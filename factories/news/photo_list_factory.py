from vk_service.models.news.photo import Photo


class PhotoListFactory:
    def build(self, values):
        return [Photo(value) for value in values]
