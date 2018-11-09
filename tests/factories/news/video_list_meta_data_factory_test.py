import unittest

from vk_service.factories.news.video_list_meta_data_factory import VideoListMetaDataFactory
from vk_service.models.news.video_list_meta_data import VideoListMetaData
from vk_service.models.news.video import Video


class VideoListMetaDataFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = VideoListMetaDataFactory()
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
        self.videos = [self.video.copy()]
        self.values = {'count': 1, 'items': self.videos.copy()}
        self.submodels = {
            'items': Video
        }

    def test_factory_build(self):
        values = self.values.copy()
        videos = self.factory.build(values)
        for key in self.submodels:
            values[key] = videos.__dict__[key]
        for key in self.submodels:
            for item in videos.__dict__[key]:
                self.assertIsInstance(item, self.submodels[key])
        self.assertIsInstance(videos, VideoListMetaData)
        self.assertEqual(videos.__dict__, values)


if __name__ == '__main__':
    unittest.main()
