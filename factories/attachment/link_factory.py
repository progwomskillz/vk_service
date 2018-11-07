from vk_service.models.attachment import Link


class LinkFactory:
    def build(self, values):
        return Link(values)
