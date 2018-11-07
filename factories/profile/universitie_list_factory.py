from vk_service.models.profile.universitie import Universitie


class UniversitieListFactory:
    def build(self, values):
        return [Universitie(value) for value in values]
