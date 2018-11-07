import unittest

from vk_service.factories.attachment.video_factory import VideoFactory
from vk_service.models.attachment.video import Video


class VideoFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = VideoFactory()
        self.values = {
            'id': 5, 'owner_id': 53, 'title': 'MyVideo', 'description': 'None',
            'duration': 47, 'photo_130': 'http://example.com/130/',
            'photo_320': 'http://example.com/320/', 'date': 2525256252,
            'adding_date': 2525256253, 'views': 14, 'comments': 84,
            'player': 'http://example.com/player/', 'can_edit': 1,
            'can_add': 1, 'access_key': 'sadasdassfwefwecw'
        }

    def test_factory_build(self):
        values = self.values.copy()
        video = self.factory.build(values)
        self.assertIsInstance(video, Video)
        self.assertEqual(video.__dict__, values)


if __name__ == '__main__':
    unittest.main()
