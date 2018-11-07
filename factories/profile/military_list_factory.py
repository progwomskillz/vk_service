from vk_service.models.profile.military import Military


class MilitaryListFactory:
    def build(self, values):
        return [Military(value) for value in values]
