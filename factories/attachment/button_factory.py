from vk_service.models.attachment.button import Button


class ButtonFactory:
    def build(self, values):
        return Button(values)
