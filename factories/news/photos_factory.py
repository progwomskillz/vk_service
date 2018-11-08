from vk_service.models.news.photos import Photos


class PhotosFactory:
    def build(self, values):
        return Photos(values)
