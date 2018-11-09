from vk_service.models.news.repost_source_post import RepostSourcePost


class RepostSourcePostListFactory:
    def build(self, posts, profiles, groups):
        return [RepostSourcePost(post, profiles, groups) for post in posts]
