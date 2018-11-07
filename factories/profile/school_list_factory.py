from vk_service.models.profile.school import School


class SchoolListFactory:
    def build(self, values):
        return [School(value) for value in values]
