from vk_service.models.profile.country import Country


class CountryFactory:
    def build(self, values):
        return Country(values)
