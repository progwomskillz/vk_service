from vk_service.models.group.city import City


class CityFactory:
    def build(self, values):
        return City(values)
