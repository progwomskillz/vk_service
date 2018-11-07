from .group_info import GroupInfo
from vk_service.factories.attachment.image_list_factory import ImageListFactory


class Cover(GroupInfo):
    def __init__(self, values):
        factories = {
            'images': ImageListFactory()
        }
        super(Cover, self).__init__(values, factories)
