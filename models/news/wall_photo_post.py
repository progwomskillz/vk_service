from .post import Post
from vk_service.factories.news.photo_list_meta_data_factory import PhotoListMetaDataFactory


class WallPhotoPost(Post):
    def __init__(self, post, profiles, groups):
        factories = {
            'photos': PhotoListMetaDataFactory()
        }
        super(WallPhotoPost, self).__init__(post, profiles, groups, factories)
