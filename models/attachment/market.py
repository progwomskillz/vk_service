from .attachment import Attachment
from vk_service.factories.attachment.price_factory import PriceFactory
from vk_service.factories.attachment.category_factory import CategoryFactory
from vk_service.factories.attachment.photo_list_factory import PhotoListFactory
from vk_service.factories.attachment.like_factory import LikeFactory


class Market(Attachment):
    def __init__(self, values):
        factories = {
            'price': PriceFactory(),
            'category': CategoryFactory(),
            'photos': PhotoListFactory(),
            'likes': LikeFactory(),
        }
        super(Market, self).__init__(values, factories)
