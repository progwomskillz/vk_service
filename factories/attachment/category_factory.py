from vk_service.models.attachment import Category


class CategoryFactory:
    def build(self, values):
        return Category(values)
