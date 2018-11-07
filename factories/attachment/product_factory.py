from vk_service.models.attachment.product import Product


class ProductFactory:
    def build(self, values):
        return Product(values)
