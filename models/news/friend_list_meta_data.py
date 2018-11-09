from vk_service.models.common.common import Common
from vk_service.factories.news.friend_list_factory import FriendListFactory


class FriendListMetaData(Common):
    def __init__(self, values):
        factories = {
            'items': FriendListFactory()
        }
        super(FriendListMetaData, self).__init__(values, factories)
