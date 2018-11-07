from vk_service.models.attachment import Button


class ButtonFactory:
    def build(self, values):
        return Button(values)
