from vk_service.models.news.post_source import PostSource


class PostSourceFactory:
    def build(self, values):
        return PostSource(values)
