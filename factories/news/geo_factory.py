from vk_service.models.news.geo import Geo


class GeoFactory:
    def build(self, values):
        return Geo(values)
