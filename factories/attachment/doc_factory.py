from vk_service.models.attachment import Doc


class DocFactory:
    def build(self, values):
        return Doc(values)
