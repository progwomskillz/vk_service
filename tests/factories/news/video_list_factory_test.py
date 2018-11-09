import unittest

from vk_service.factories.news.video_list_factory import VideoListFactory
from vk_service.models.news.video import Video
from vk_service.models.news.like import Like
from vk_service.models.news.repost import Repost


class VideoListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = VideoListFactory()
        self.like = {'user_likes': 0, 'count': 5}
        self.repost = {'count': 5, 'user_reposted': 0}
        self.video = {
            'id': 456242504, 'owner_id': -30666517, 'title': 'Highload++',
            'duration': 0, 'description': 'Ссылка: https://tprg.ru/x3iB',
            'date': 1541750162, 'comments': 140, 'views': 81050,
            'width': 1280,  'height': 720,
            'photo_130': 'https://pp.userap...a39/hSJ7265fPik.jpg',
            'photo_320': 'https://pp.userap...a37/erWB1hglgrs.jpg',
            'photo_800': 'https://pp.userap...a35/PCiEykYG7_Y.jpg',
            'photo_1280': 'https://pp.userap...a36/S-2i3rzvcps.jpg',
            'access_key': '6627f0cc8fab088de5',
            'live': 1, 'spectators': 523,
            'first_frame_800': 'https://pp.userap...2b3/J0vvDsbM_pY.jpg',
            'first_frame_320': 'https://pp.userap...2b4/Cgga3761OLM.jpg',
            'first_frame_160': 'https://pp.userap...2b5/V1siEEwv2xo.jpg',
            'first_frame_130': 'https://pp.userap...2b6/P5QNkFK4jTI.jpg',
            'can_add': 1, 'can_comment': 1, 'can_repost': 1,
            'likes': self.like.copy(), 'reposts': self.repost.copy()
        }
        self.values = [self.video.copy()]
        self.submodels = {
            'likes': Like,
            'reposts': Repost
        }

    def test_factory_build(self):
        values = self.values.copy()
        videos = self.factory.build(values)
        self.assertIsInstance(videos, list)
        for i, video in enumerate(videos):
            self.assertIsInstance(video, Video)
            for key in self.submodels:
                values[i][key] = video.__dict__[key]
            for key in self.submodels:
                self.assertIsInstance(video.__dict__[key], self.submodels[key])
            self.assertEqual(video.__dict__, values[i])


if __name__ == '__main__':
    unittest.main()
