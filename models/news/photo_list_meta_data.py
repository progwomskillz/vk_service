from vk_service.models.common.common import Common
from vk_service.factories.news.photo_list_factory import PhotoListFactory


class PhotoListMetaData(Common):
    def __init__(self, values):
        factories = {
            'items': PhotoListFactory()
        }
        super(PhotoListMetaData, self).__init__(values, factories)
