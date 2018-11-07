from vk_service.models.group.place import Place


class PlaceFactory:
    def build(self, values):
        return Place(values)
