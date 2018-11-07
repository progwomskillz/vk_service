from vk_service.models.attachment.action import Action


class ActionFactory:
    def build(self, values):
        return Action(values)
