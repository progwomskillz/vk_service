from vk_service.models.news.friend_list_meta_data import FriendListMetaData


class FriendListMetaDataFactory:
    def build(self, values):
        return FriendListMetaData(values)
