from .attachment import Attachment
from vk_service.factories.attachment import (
    PriceFactory, CategoryFactory, PhotoListFactory, LikeFactory
)


class Market(Attachment):
    def __init__(self, values):
        factories = {
            'price': PriceFactory(),
            'category': CategoryFactory(),
            'photos': PhotoListFactory(),
            'likes': LikeFactory(),
        }
        super(Market, self).__init__(values, factories)
