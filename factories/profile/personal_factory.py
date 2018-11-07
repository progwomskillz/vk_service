from vk_service.models.profile.personal import Personal


class PersonalFactory:
    def build(self, values):
        return Personal(values)
