from vk_service.models.attachment.market_album import MarketAlbum


class MarketAlbumFactory:
    def build(self, values):
        return MarketAlbum(values)
