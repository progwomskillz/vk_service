from vk_service.models.group.crop import Crop


class CropFactory:
    def build(self, values):
        return Crop(values)
