from vk_service.models.group.group import Group


class GroupListFactory:
    def build(self, values):
        return [Group(value) for value in values]
