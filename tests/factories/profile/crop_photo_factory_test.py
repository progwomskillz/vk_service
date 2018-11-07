import unittest

from vk_service.factories.profile.crop_photo_factory import CropPhotoFactory
from vk_service.models.profile.crop_photo import CropPhoto
from vk_service.models.profile.photo import Photo
from vk_service.models.profile.crop import Crop
from vk_service.models.profile.rect import Rect


class CropPhotoFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = CropPhotoFactory()
        self.photo = {'id': 5}
        self.crop = {'x': 1, 'y': 1, 'x2': 99, 'y2': 99}
        self.rect = {'x': 1, 'y': 1, 'x2': 99, 'y2': 99}
        self.values = {
            'photo': self.photo.copy(),
            'crop': self.crop.copy(),
            'rect': self.rect.copy()
        }
        self.submodels = {
            'photo': Photo,
            'crop': Crop,
            'rect': Rect
        }

    def test_factory_build(self):
        values = self.values.copy()
        crop_photo = self.factory.build(values)
        self.assertIsInstance(crop_photo, CropPhoto)
        for key in self.submodels:
            values[key] = crop_photo.__dict__[key]
        for key in self.submodels:
            value = self.submodels[key]
            self.assertIsInstance(crop_photo.__dict__[key], value)
        self.assertEqual(crop_photo.__dict__, values)


if __name__ == '__main__':
    unittest.main()
