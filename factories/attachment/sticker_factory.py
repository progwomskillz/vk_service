from vk_service.models.attachment.sticker import Sticker


class StickerFactory:
    def build(self, values):
        return Sticker(values)
