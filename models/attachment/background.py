from .attachment import Attachment
from vk_service.factories.attachment import ImageListFactory, PointListFactory


class Background(Attachment):
    def __init__(self, values):
        factories = {
            'images': ImageListFactory(),
            'points': PointListFactory(),
        }
        super(Background, self).__init__(values, factories)
