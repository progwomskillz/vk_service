from vk_service.models.profile.profile import Profile


class ProfileListFactory:
    def build(self, values):
        return [Profile(value) for value in values]
