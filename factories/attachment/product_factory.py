from vk_service.models.attachment import Product


class ProductFactory:
    def build(self, values):
        return Product(values)
