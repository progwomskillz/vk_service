from vk_service.models.profile.occupation import Occupation


class OccupationFactory:
    def build(self, values):
        return Occupation(values)
