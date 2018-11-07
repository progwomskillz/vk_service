from vk_service.models.attachment.link import Link


class LinkFactory:
    def build(self, values):
        return Link(values)
