from vk_service.models.profile.city import City


class CityFactory:
    def build(self, values):
        return City(values)
