from .post import Post
from vk_service.factories.news.photos_factory import PhotosFactory


class WallPhotoPost(Post):
    def __init__(self, post, profiles, groups):
        factories = {
            'photos': PhotosFactory()
        }
        super(TextPost, self).__init__(post, profiles, groups, factories)
