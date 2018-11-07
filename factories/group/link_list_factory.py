from vk_service.models.group.link import Link


class LinkListFactory:
    def build(self, values):
        return [Link(value) for value in values]
