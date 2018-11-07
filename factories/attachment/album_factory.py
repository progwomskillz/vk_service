from vk_service.models.attachment.album import Album


class AlbumFactory:
    def build(self, values):
        return Album(values)
