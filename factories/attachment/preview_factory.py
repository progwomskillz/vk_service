from vk_service.models.attachment import Preview


class PreviewFactory:
    def build(self, values):
        return Preview(values)
