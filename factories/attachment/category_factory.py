from vk_service.models.attachment.category import Category


class CategoryFactory:
    def build(self, values):
        return Category(values)
