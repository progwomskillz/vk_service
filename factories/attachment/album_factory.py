from vk_service.models.attachment import Album


class AlbumFactory:
    def build(self, values):
        return Album(values)
