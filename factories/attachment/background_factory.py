from vk_service.models.attachment.background import Background


class BackgroundFactory:
    def build(self, values):
        return Background(values)
