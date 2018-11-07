from vk_service.models.attachment.poll import Poll


class PollFactory:
    def build(self, values):
        return Poll(values)
