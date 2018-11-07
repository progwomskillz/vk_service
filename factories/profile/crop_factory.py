from vk_service.models.profile.crop import Crop


class CropFactory:
    def build(self, values):
        return Crop(values)
