from vk_service.models.group.crop_photo import CropPhoto


class CropPhotoFactory:
    def build(self, values):
        return CropPhoto(values)
