from vk_service.models.news.wall_photo_post import WallPhotoPost


class WallPhotoPostFactory:
    def build(self, post, profiles, groups):
        return WallPhotoPost(post, profiles, groups)
