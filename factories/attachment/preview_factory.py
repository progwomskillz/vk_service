from vk_service.models.attachment.preview import Preview


class PreviewFactory:
    def build(self, values):
        return Preview(values)
