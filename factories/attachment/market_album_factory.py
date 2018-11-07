from vk_service.models.attachment import MarketAlbum


class MarketAlbumFactory:
    def build(self, values):
        return MarketAlbum(values)
