from vk_service.models.common import Photo
from vk_service.factories.attachment import SizeListFactory


class Photo(Photo):
    def __init__(self, values):
        factories = {
            'sizes': SizeListFactory()
        }
        super(Photo, self).__init__(values, factories)
