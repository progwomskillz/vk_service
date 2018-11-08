from vk_service.models.profile.profile import Profile


class ProfileFactory:
    def build(self, values):
        return Profile(values)
