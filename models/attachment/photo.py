from vk_service.models.common.photo import Photo
from vk_service.factories.attachment.size_list_factory import SizeListFactory


class Photo(Photo):
    def __init__(self, values):
        factories = {
            'sizes': SizeListFactory()
        }
        super(Photo, self).__init__(values, factories)
