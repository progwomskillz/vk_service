from vk_service.models.group.ban import Ban


class BanFactory:
    def build(self, values):
        return Ban(values)
