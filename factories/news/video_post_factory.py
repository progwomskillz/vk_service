from vk_service.models.news.video_post import VideoPost


class VideoPostFactory:
    def build(self, post, profiles, groups):
        return VideoPost(post, profiles, groups)
