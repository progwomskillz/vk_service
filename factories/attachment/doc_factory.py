from vk_service.models.attachment.doc import Doc


class DocFactory:
    def build(self, values):
        return Doc(values)
