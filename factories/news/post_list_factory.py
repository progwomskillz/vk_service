from .text_post_factory import TextPostFactory
from .wall_photo_post_factory import WallPhotoPostFactory
from .friend_post_factory import FriendPostFactory
from .video_post_factory import VideoPostFactory


class PostListFactory:
    def build(self, values):
        newsfeed = values['items']
        profiles = values['profiles']
        groups = values['groups']
        posts = []
        factories = {
            'post': TextPostFactory(),
            'wall_photo': WallPhotoPostFactory(),
            'friend': FriendPostFactory(),
            'video': VideoPostFactory()
        }
        for news in newsfeed:
            if news['type'] in factories:
                factory = factories[news['type']]
                post = factory.build(news, profiles, groups)
                posts.append(post)
        return posts
