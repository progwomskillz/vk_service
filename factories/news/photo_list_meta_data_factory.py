from vk_service.models.news.photo_list_meta_data import PhotoListMetaData


class PhotoListMetaDataFactory:
    def build(self, values):
        return PhotoListMetaData(values)
