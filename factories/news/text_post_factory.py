from vk_service.models.news.text_post import TextPost


class TextPostFactory:
    def build(self, post, profiles, groups):
        return TextPost(post, profiles, groups)
