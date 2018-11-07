from vk_service.models.attachment import Poll


class PollFactory:
    def build(self, values):
        return Poll(values)
