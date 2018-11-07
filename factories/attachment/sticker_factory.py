from vk_service.models.attachment import Sticker


class StickerFactory:
    def build(self, values):
        return Sticker(values)
