from vk_service.models.group.group import Group


class GroupFactory:
    def build(self, values):
        return Group(values)
