from vk_service.models.news.comment import Comment


class CommentFactory:
    def build(self, values):
        return Comment(values)
