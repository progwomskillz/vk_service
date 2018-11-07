from vk_service.models.profile.career import Career


class CareerListFactory:
    def build(self, values):
        return [Career(value) for value in values]
