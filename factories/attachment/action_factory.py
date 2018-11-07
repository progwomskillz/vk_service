from vk_service.models.attachment import Action


class ActionFactory:
    def build(self, values):
        return Action(values)
