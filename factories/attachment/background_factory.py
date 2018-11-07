from vk_service.models.attachment import Background


class BackgroundFactory:
    def build(self, values):
        return Background(values)
