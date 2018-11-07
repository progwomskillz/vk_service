from vk_service.models.common.crop_photo import CropPhoto
from vk_service.factories.group.photo_factory import PhotoFactory
from vk_service.factories.group.crop_factory import CropFactory
from vk_service.factories.group.rect_factory import RectFactory


class CropPhoto(CropPhoto):
    def __init__(self, values):
        factories = {
            'photo': PhotoFactory(),
            'crop': CropFactory(),
            'rect': RectFactory()
        }
        super(CropPhoto, self).__init__(values, factories)
