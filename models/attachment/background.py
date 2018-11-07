from .attachment import Attachment
from vk_service.factories.attachment.image_list_factory import ImageListFactory
from vk_service.factories.attachment.point_list_factory import PointListFactory


class Background(Attachment):
    def __init__(self, values):
        factories = {
            'images': ImageListFactory(),
            'points': PointListFactory(),
        }
        super(Background, self).__init__(values, factories)
