from vk_service.models.group.country import Country


class CountryFactory:
    def build(self, values):
        return Country(values)
