from .text_post_factory import TextPostFactory
from .wall_photo_post_factory import WallPhotoPostFactory
from .friend_post_factory import FriendPostFactory
from .video_post_factory import VideoPostFactory


class PostListFactory:
    def build(self, values, profiles, groups):
        posts = []
        factories = {
            'post': TextPostFactory(),
            'wall_photo': WallPhotoPostFactory(),
            'friend': FriendPostFactory(),
            'video': VideoPostFactory()
        }
        for value in values:
            if value['type'] in factories:
                factory = factories[value['type']]
                post = factory.build(value, profiles, groups)
                posts.append(post)
        return posts
